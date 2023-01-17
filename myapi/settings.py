INSTALLED_APPS = [
    'rest_framework',
    'myapi.apps.MyapiConfig',
    'telebot.apps.TelebotConfig',
    'price.apps.PriceConfig',
    'cms.apps.CmsConfig',
    'crm.apps.CrmConfig', #добавили класс из нового приложения
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]