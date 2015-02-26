from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Brewery, Taps
from .serializers import BrewerySerializer, TapsListSerializer, TapsSerializer


class BreweryListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer


class TapsMixin(object):
    permission_classes = [IsAuthenticated]
    queryset = Taps.objects.all()


class TapsCreate(TapsMixin, generics.CreateAPIView):
    serializer_class = TapsSerializer


class TapsDetail(TapsMixin, generics.RetrieveAPIView):
    """Returns a specific tap"""
    serializer_class = TapsListSerializer


class TapsList(TapsMixin, generics.ListAPIView):
    """Returns a list of all of the taps"""
    serializer_class = TapsListSerializer
