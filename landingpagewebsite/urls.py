
"""
#I - маршрутизатор проверяет путь, который запросил пользователь,
далее - попадаем во views.py в определенную функцию
landingpagewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from landingpagewebsite.routers import router, simrouter

#Импорт файла с функцией из crm
from crm import views
# from myapi import views

'''Прописываем пути определенных страниц, в которые мы передаем значение
через файл views (в нем функции, из которых мы впоследствии вытаскиваем
данные из БД)'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('thanks/', views.thanks_page, name='thanks_page'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

