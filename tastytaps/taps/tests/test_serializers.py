from django.test import TestCase

from tastytaps.taps.models import Brewery, Price
from tastytaps.taps.serializers import (BrewerySerializer, PriceSerializer,
                                        TapsSerializer)


class TestBaseSerializer(TestCase):
    def setUp(self):
        self.serializer = None
        self.data = {}

    def success_serialize(self):
        self.assertTrue(self.serializer(data=self.data).is_valid())

    def error_serialize(self):
        self.assertFalse(self.serializer(data=self.data).is_valid())


class TestBrewerySerializer(TestBaseSerializer):
    def setUp(self):
        super(TestBrewerySerializer, self).setUp()
        self.serializer = BrewerySerializer
        self.data = {'name': 'Oakshire Brewing', 'city': 'Eugene'}

    def test_success_serialize(self):
        return self.success_serialize()

    def test_error_serialize(self):
        del self.data['name']
        return self.error_serialize()


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
        brewery = Brewery.objects.create(name='Ninkasi', city='Eugene')
        price = Price.objects.create(size='Glass', price=4.99)

        self.data = {
            'name': 'Tastybrew tap list',
            'summary': 'Taps summary',
            'brewery': brewery.pk,
            'style': 'Flanders red ale',
            'price': price.pk
        }

    def test_success_serialize(self):
        return self.success_serialize()
