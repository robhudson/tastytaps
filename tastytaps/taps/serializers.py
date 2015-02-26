from rest_framework.serializers import ModelSerializer

from .models import Brewery, Price, Taps


class BrewerySerializer(ModelSerializer):
    class Meta:
        model = Brewery


class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price


class TapsSerializer(ModelSerializer):
    class Meta:
        model = Taps


class TapsListSerializer(TapsSerializer):
    brewery = BrewerySerializer()
    price = PriceSerializer()
