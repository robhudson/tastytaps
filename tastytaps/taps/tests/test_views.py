from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase


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

    # TODO: test delete tap
    # TODO: test update tap (change price)

    def test_unauthenticated(self):
        url = reverse('taps-list')
        self.client.force_authenticate(user=None)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 403)

    def test_create(self):
        url = reverse('taps-list')
        data = {
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
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
        # TODO: assert response content
        # TODO: assert resource URL
