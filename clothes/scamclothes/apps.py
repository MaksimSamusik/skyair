from django.apps import AppConfig


class ScamclothesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scamclothes'
    verbose_name = 'Рейсы'

    def ready(self):
        import scamclothes.signals