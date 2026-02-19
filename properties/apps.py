from django.apps import AppConfig

class PropertiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "properties"

    def ready(self):
        # ensure signals are registered
        import properties.signals
