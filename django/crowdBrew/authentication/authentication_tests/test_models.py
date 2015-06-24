from django.test import TestCase
from authentication.models import Account

class BrewTestCase(TestCase):
    def setUp(self):
        account1 = Account.objects.create(email="user1@test.com",username="username1",first_name="First", last_name="Last", tagline="The First User")

    def test_account_persist(self):
        """Tests persist of valid account"""
        account = Account.objects.get(username="username1")
        self.assertEqual(account.email, "user1@test.com")
        self.assertEqual(account.first_name, "First")
        self.assertEqual(account.last_name, "Last")
        self.assertEqual(account.get_full_name(), "First Last")
        self.assertEqual(account.tagline, "The First User")
