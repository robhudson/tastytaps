import json

from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase

from tastytaps.taps.models import Price, Taps


class TestTapsViewSet(APITestCase):

    def setUp(self):
        super(TestTapsViewSet, self).setUp()
        credentials = {
            'username': 'tester',
            'password': 'password',
        }
        self.user = User.objects.create(**credentials)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.data = {
            'name': 'Duchesse de Bourgogne',
            'style': 'Flanders Red Ale',
            'summary': 'A wonderful Flanders Red Ale',
            'brewery_name': 'Brouwerij Verhaeghe',
            'brewery_country': 'Belgium',
            'prices': [
                {'size': 'Glass', 'price': '3.50'},
                {'size': 'Pint', 'price': '5.00'},
            ],
        }

    # TODO: test delete tap

    def _make_tap(self):
        data = self.data.copy()
        prices = data.pop('prices')
        tap = Taps.objects.create(**data)
        for price in prices:
            Price.objects.create(tap=tap, **price)
        return tap

    def test_unauthenticated(self):
        self.client.force_authenticate(user=None)
        resp = self.client.get('/api/v1/taps/')
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        tap = self._make_tap()
        resp = self.client.get('/api/v1/taps/%s/' % tap.id)
        for key in self.data.keys():
            self.assertEqual(resp.data[key], self.data[key],
                             'Unexpected value for key:%s: %s' % (
                                 key, resp.data[key]))

    def test_create(self):
        resp = self.client.post('/api/v1/taps/', self.data, format='json')
        self.assertEqual(resp.status_code, 201)

        # Using json here b/c `resp.data` nested structure gets converted to an
        # `OrderedDict` and doesn't match.
        data = json.loads(resp.content)
        for key in self.data.keys():
            self.assertEqual(data[key], self.data[key],
                             'Unexpected value for key:%s: %s' % (
                                 key, data[key]))

    def test_update(self):
        tap = self._make_tap()
        new_data = self.data.copy()
        # Update summary, remove Pint option, and increase glass price.
        new_data.update({
            'summary': 'An awesome Flanders Red Ale',
            'prices': [
                {'size': 'Glass', 'price': '4.00'},
            ],
        })
        resp = self.client.put('/api/v1/taps/%s/' % tap.id, new_data,
                               format='json')
        data = json.loads(resp.content)
        for key in new_data.keys():
            self.assertEqual(data[key], new_data[key],
                             'Unexpected value for key:%s: %s' % (
                                 key, new_data[key]))
        self.assertEqual(tap.prices.count(), 1)
