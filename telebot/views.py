from django.shortcuts import render

from telebot.models import TeleSettings
from rest_framework.viewsets import ModelViewSet
from telebot.serializers import TeleSettingsSerializer
# Create your views here.

class TeleSettingsViewSet(ModelViewSet):
    queryset = TeleSettings.objects.all()
    serializer_class = TeleSettingsSerializer