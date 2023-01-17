from rest_framework import serializers
from price.models import PriceCard, PriceTable

class PriceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCard
        fields = '__all__'

class PriceTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceTable
        fields = '__all__'