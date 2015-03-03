from rest_framework.permissions import IsAuthenticated

from .models import Brewery, Price, Taps
from .serializers import (BrewerySerializer, PriceSerializer, TapsSerializer,
                          TapsListSerializer)

from rest_framework.viewsets import ModelViewSet


class BreweryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer


class PriceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class TapsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Taps.objects.all()

    def get_serializer_class(self):
        """Returns the right serializer class based on action"""
        if self.action == 'create':
            return TapsSerializer
        return TapsListSerializer
