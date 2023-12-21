from django.apps import AppConfig

class OmniCatalogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.omni_catalog"

    def ready(self): # for signals.
        import apps.omni_catalog.signals.omnibus_signals