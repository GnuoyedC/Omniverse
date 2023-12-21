from marvel_api_handler import MarvelAPI
from apps.omni_catalog.models import Omnibus
from model_helpers import ModelHelper

class APIDBHandler:

    @classmethod
    def poll_and_save_all_comics(cls):
        total_comics_count_from_marvel_api = MarvelAPI.get_all_comics_count()
        total_omnibus_entries_in_db = Omnibus.objects.count()
        if total_omnibus_entries_in_db != total_comics_count_from_marvel_api:
            poll_limit = 2000
            multiples_comics_in_marvel_api = total_comics_count_from_marvel_api  // poll_limit
            multiples_omnibus_db_entries = total_omnibus_entries_in_db // poll_limit


            for multiple_count in range(multiples_omnibus_db_entries,
            multiples_comics_in_marvel_api):
                APIDBHandler.save_results(MarvelAPI.get_comics_passed_params(
                    offset=(poll_limit * multiple_count),
                    poll_limit=poll_limit))
    @classmethod
    def save_results(cls, result_set:list):
        ModelHelper.save_all_results_to_model(result_list=result_set,model=Omnibus())

if __name__ == '__main__':
    APIDBHandler.poll_and_save_all_comics()