from django.test import TestCase

from tastytaps.taps.models import Price
from tastytaps.taps.serializers import PriceSerializer, TapsSerializer


class TestBaseSerializer(TestCase):
    def setUp(self):
        self.serializer = None
        self.data = {}

    def success_serialize(self):
        self.assertTrue(self.serializer(data=self.data).is_valid())

    def error_serialize(self):
        self.assertFalse(self.serializer(data=self.data).is_valid())


class TestPriceSerializer(TestBaseSerializer):
    def setUp(self):
        super(TestPriceSerializer, self).setUp()
        self.serializer = PriceSerializer
        self.data = {'size': 'Pint', 'price': 5.99}

    def test_success_serialize(self):
        return self.success_serialize()

    def test_error_serialize(self):
        del self.data['price']
        return self.error_serialize()


class TestTapsSerializer(TestBaseSerializer):
    def setUp(self):
        super(TestTapsSerializer, self).setUp()
        self.serializer = TapsSerializer
        price = Price.objects.create(size='Glass', price=4.99)

        self.data = {
            'name': 'Tastybrew tap list',
            'summary': 'Taps summary',
            'style': 'Flanders red ale',
            'price': price.pk,
            'brewery_name': 'Oakshire'
        }

    def test_success_serialize(self):
        return self.success_serialize()
