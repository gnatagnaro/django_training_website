from django.shortcuts import render

from cms.models import CmsSlider
from rest_framework.viewsets import ModelViewSet
from cms.serializers import CmsSliderSerializer
# Create your views here.

class CmsSliderViewSet(ModelViewSet):
    queryset = CmsSlider.objects.all()
    serializer_class = CmsSliderSerializer