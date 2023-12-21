from utils.helper_functions import cleanse_extraneous_hyphens
from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.omni_catalog.models import Omnibus

@receiver(pre_save, sender=Omnibus)
def omnibus_presave(sender, instance, **kwargs):
    instance.modified = cleanse_extraneous_hyphens(instance.modified)