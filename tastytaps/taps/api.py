from rest_framework.permissions import IsAuthenticated

from .models import Price, Taps
from .serializers import (PriceSerializer, TapsSerializer, TapsListSerializer)

from rest_framework.viewsets import ModelViewSet


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
