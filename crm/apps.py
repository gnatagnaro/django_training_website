from django.apps import AppConfig

# Импортируем название этого класса в сеттингс


class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm'
