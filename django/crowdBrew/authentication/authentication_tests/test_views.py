from rest_framework.test import APITestCase, APIClient

class ViewTestCase(APITestCase):
    fixtures = ['authentication_testdata.json']
    def setUp(self):
        self.client = APIClient()

    def test_accounts_view(self):
        # Issue a GET request.
        response = self.client.get('/app/api/v1/accounts/', format='json')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 6 accounts.
        self.assertEqual(len(response.data), 6)

    def test_account_view(self):
        # Issue a GET request.
        response = self.client.get('/app/api/v1/accounts/cbuser1/', format='json')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the tagline of the first brewer is correct.
        self.assertEqual(response.data['tagline'], "The Original Crowd Brewer")