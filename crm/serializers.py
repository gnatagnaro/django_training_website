from rest_framework import serializers
from crm.models import Order, StatusCrm, CommentCrm

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class StatusCrmSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCrm
        fields = '__all__'

class CommentCrmSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentCrm
        fields = '__all__'