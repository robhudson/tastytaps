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

    def create(self, validated_data):
        prices_data = validated_data.pop('prices')
        tap = Taps.objects.create(**validated_data)
        for price in prices_data:
            Price.objects.create(tap=tap, **price)
        return tap


class TapsListSerializer(TapsSerializer):
    price = PriceSerializer()
