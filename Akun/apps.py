from django.apps import AppConfig


class AkunConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Akun'

    def ready(self):
        import Akun.signals
