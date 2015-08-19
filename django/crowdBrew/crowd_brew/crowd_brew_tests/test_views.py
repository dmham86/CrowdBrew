from rest_framework.test import APITestCase, APIClient
import os.path
from authentication.models import Account
from crowd_brew.models import *

class ViewTestCase(APITestCase):
    fixtures = [os.path.join(os.path.dirname(__file__), '..\\..\\authentication\\fixtures\\authentication_testdata.json').replace('\\','/'), 'crowd_brew_testdata.json']
    def setUp(self):
        self.client = APIClient()

    def test_index_view(self):
        # Issue a GET request.
        response = self.client.get('/app/api/v1/brews/', format='json')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 8 brews
        self.assertEqual(len(response.data), 8)

    def test_brewer_view(self):
        # Issue a GET request.
        response = self.client.get('/app/api/v1/accounts/cbuser1/brews/', format='json')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the brewer has 5 brews.
        self.assertEqual(len(response.data), 5)

    def test_brew_view(self):
        brew_id = str(1)
        # Issue a GET request.
        response = self.client.get('/app/api/v1/brews/' + brew_id + '/', format='json')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Confirm the correct brew was returned
        self.assertEqual(response.data["name"],'Number One Cascadian')
