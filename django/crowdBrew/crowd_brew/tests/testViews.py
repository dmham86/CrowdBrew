from rest_framework.test import APITestCase, APIClient
from authentication.models import Account
from crowd_brew.models import *

class ViewTestCase(APITestCase):
    fixtures = ['authentication_testdata.json', 'crowd_brew_testdata.json']
    def setUp(self):
        self.client = APIClient()

    def test_index_view(self):
        # Issue a GET request.
        response = self.client.get('/app/api/v1/brews/', format='json')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.data), 8)

    def test_brewer_view(self):
        # Issue a GET request.
        response = self.client.get('/app/api/v1/accounts/cbuser1/', format='json')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(response.data['tagline'], "The Original Crowd Brewer")

        # Issue a GET request.
        response = self.client.get('/app/api/v1/accounts/cbuser1/brews/', format='json')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.data), 5)