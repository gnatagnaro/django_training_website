from rest_framework import serializers
from telebot.models import TeleSettings

class TeleSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeleSettings
        fields = '__all__'