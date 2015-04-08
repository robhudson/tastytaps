from rest_framework.serializers import ModelSerializer

from .models import Price, Taps


class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = ('size', 'price')


class TapsSerializer(ModelSerializer):
    prices = PriceSerializer(many=True)

    class Meta:
        model = Taps


class TapsListSerializer(TapsSerializer):
    price = PriceSerializer()
