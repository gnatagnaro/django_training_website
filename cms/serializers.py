from rest_framework import serializers
from cms.models import CmsSlider

class CmsSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmsSlider
        fields = '__all__'