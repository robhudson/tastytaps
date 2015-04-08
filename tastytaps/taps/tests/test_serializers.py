from django.test import TestCase

from tastytaps.taps.serializers import TapsSerializer


class TestTapsSerializer(TestCase):
    def setUp(self):
        super(TestTapsSerializer, self).setUp()

        self.data = {
            'name': 'Duchesse de Bourgogne',
            'style': 'Flanders Red Ale',
            'summary': 'A wonderful Flanders Red Ale',
            'brewery_name': 'Brouwerij Verhaeghe',
            'brewery_country': 'Belgium',
            'prices': [
                {'size': 'Glass', 'price': 3.50},
                {'size': 'Pint', 'price': 5.00},
            ],
        }

    def test_serialize(self):
        self.assertTrue(TapsSerializer(data=self.data).is_valid())
