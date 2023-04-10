from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # run essential (and heavier) queries at startup
    def ready(self):
        pass
        # import constants
