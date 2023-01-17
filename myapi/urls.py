# myapi/urls.py
from django.urls import path
from rest_framework import routers
from . import views
from django.conf import urls
# from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', urls.include(router.urls)),
    path('api-auth/', urls.include('rest_framework.urls', namespace='rest_framework'))
]