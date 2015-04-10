from django.test import TestCase

from tastytaps.taps.models import Taps
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

    def serializer(self):
        return TapsSerializer(data=self.data)

    def test_serialize(self):
        self.assertTrue(self.serializer().is_valid())

    def test_required_fields(self):
        required_fields = ('name', 'style', 'summary', 'prices')
        for field in required_fields:
            del self.data[field]
            serializer = self.serializer()
            self.assertFalse(serializer.is_valid())
            self.assertEqual(serializer.errors.get(field)[0],
                             u'This field is required.')

    def test_name(self):
        del self.data['prices']
        taps = Taps(**self.data)
        serializer = TapsSerializer(instance=taps)
        self.assertEqual(serializer.data['name'], u'Duchesse de Bourgogne')
