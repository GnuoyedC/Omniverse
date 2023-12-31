from django.db.models import (
    Model,
    Max
)
from django.forms.models import model_to_dict
from typing import Type,List,Dict,Any
from json_handler import JsonHandler as h_json
from helper_functions import (
    remove_special_characters_and_normalize,
    uniquify_list
)
from exceptions.model_helpers_exceptions import (
    ModelNotPassed,
    ModelHasNoFields,
    AttrNotFound
)
from date_helpers import (
    DATEFMT
)
class ModelHelper:
    @classmethod
    def get_model_as_dict(cls,model_instance:Model) -> Dict[str,Any]:
        if not model_instance:
            raise

        return model_to_dict(model_instance)

    @classmethod
    def get_model_fields(cls, model_class: Type[Model]) -> List:
        """
        returns list of model field objects (not names)

        Args:
            model (Type[base.ModelBase]): passed django model

        Raises:
            ModelNotPassed: if object is not a model, raise.

        Returns:
            List: list of model objects.
        """
        if not issubclass(model_class, Model):
            raise ModelNotPassed(model_class)

        model_fields = model_class._meta.get_fields()
        if not model_fields:
            raise ModelHasNoFields(model_class)

        return model_fields

    @classmethod
    def get_model_field_names(cls, model_class: Type[Model]) -> List[str]:
        """
        returns a list of all model field names.

        Args:
            model (Type[base.ModelBase]): passed django model.

        Returns:
            List: list of field names of the model.
        """
        return [field.name for field in cls.get_model_fields(model_class)]

    @classmethod
    def map_json_keys_to_model_attr(cls, data: Dict[str,any],
                                model_class: Type[Model]) -> Dict[str, str]:
        """
        Maps JSON keys to Django model attribute names.

        Args:
            data (Dict): The JSON data as a dictionary.
            model_class (Type[Model]): Django model class.

        Returns:
            Dict[str, str]: Mapping of model field names to JSON keys.
        """

        # store list of model field names from model.
        model_fields = cls.get_model_field_names(model_class)
        # retrieve all keys from the passed json data.
        key_list = uniquify_list(h_json.get_all_keys(data))
        new_dict = {}
        for field in model_fields:
            # removes special characters, forces lower case.
            normalized_field = remove_special_characters_and_normalize(field)
            for key in key_list:
                # this normalization is important, as it
                # will force keys like diamondCode to "diamondcode",
                # which will appear as "diamondcode" in the above, as well (which
                # will appear as diamond_code as the model attribute)
                # eliminates need for complex checking, like casing for characters.
                normalized_key = remove_special_characters_and_normalize(key)
                if normalized_key == normalized_field:
                    # if they are equal, map the field to the JSON equivalent.
                    # so, diamond_code is mapped to diamondCode.
                    new_dict[field] = key
        return new_dict

    @classmethod
    def load_dict_to_model(cls, data: Dict, model_instance: Model):
        """
        Loads data from a dictionary into a Django model
        instance based on mapped keys.

        Args:
            data (Dict): The JSON data as a dictionary.
            model_instance (Model): An instance of a Django model.
        """

        model_class = model_instance.__class__

        # gets a dictionary mapping of the model
        # attributes to the JSON counterpart, like
        # {"diamond_code": "diamondCode"}
        field_key_mapping = cls.map_json_keys_to_model_attr(data, model_class)
        # iterates over the map.
        for model_field, json_key in field_key_mapping.items():
            # checks that the model object has the passed
            # model attribute (i.e. diamond_code),
            # and that is respective value (diamondCode) exists within
            # the passed JSON data dictionary.
            if hasattr(model_instance, model_field) and json_key in data:
                # the value of the JSON key (diamondCode) would be passed
                # to the diamond_code model field on the model.
                setattr(model_instance, model_field, data[json_key])

    @classmethod
    def save_all_results_to_model(cls, result_list:List[Dict[str,Any]],
    model:Model):
        for result in result_list:
            cls.load_dict_to_model(result, model_instance=model)
            model.save()

    @classmethod
    def get_max_date(cls, date_field: str, model_class:Model) -> str:
        """
        Gets the maximum date for the date field specified,
        for the model specified.

        Args:
            date_field (str): date field for the model.
            model_class (Model): passed model.

        Raises:
            ValueError (date_field): raised if date field is not passed.
            Exception (model_class): raised if not a model class.
            AttributeError(date_field, model_class):raised if date_field is not
                                                    an attribute on model.
            ValueError (max_date): raised if max_date not found in records.

        Returns:
            str: the max date for the specified date field from the model.
        """
        if not date_field:
            raise ValueError("Date value not passed.")
        if not issubclass(model_class, Model):
            ModelNotPassed(model_class)
        if not hasattr(model_class, date_field):
            raise AttributeError(
                f"Attribute '{date_field}'not found in model {model_class}."
            )
        max_date_key = f"{date_field}__max"
        max_date = model_class.objects.aggregate(Max(
            date_field
        )).get(max_date_key)

        if max_date is None:
            raise ValueError(f"No records found for {model_class}.")
        return max_date.strftime(DATEFMT)