from rest_framework.serializers import ModelSerializer

from .models import Price, Taps


class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price


class TapsSerializer(ModelSerializer):
    class Meta:
        model = Taps


class TapsListSerializer(TapsSerializer):
    price = PriceSerializer()
