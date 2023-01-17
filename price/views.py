from price.models import PriceCard, PriceTable
from rest_framework.viewsets import ModelViewSet
from price.serializers import PriceCardSerializer, PriceTableSerializer
# Create your views here.

class PriceCardViewSet(ModelViewSet):
    queryset = PriceCard.objects.all()
    serializer_class = PriceCardSerializer

class PriceTableViewSet(ModelViewSet):
    queryset = PriceTable.objects.all()
    serializer_class = PriceTableSerializer