from django.test import TestCase
from authentication.models import Account
from crowd_brew.models import *

class BrewTestCase(TestCase):
    def setUp(self):
        account1 = Account.objects.create(email="user1@test.com",username="username1",first_name="First", last_name="Last", tagline="The First User")
        brewery1 = Brewery.objects.create(name="Brewery 1", description="Some information about Brewery 1")
        brewer1 = Brewer.objects.create(user=account1, brewery=brewery1)
        Brew.objects.create(name="Brew 1", description="This is Brew 1", style="Saison", type="Extract", abv=5, brewer=brewer1)

    def test_brewery_persist(self):
        """Tests persist of valid brewery"""
        brewery = Brewery.objects.get(name="Brewery 1")
        self.assertEqual(brewery.description, "Some information about Brewery 1")

    def test_brewer_belongs_to_brewery(self):
        """Tests that the account, brewery, and brewer were created correctly linked"""
        account = Account.objects.get(username="username1")
        brewer = Brewer.objects.get(user=account)
        self.assertEqual(brewer.brewery.name, "Brewery 1")

    def test_brew_persist(self):
        """Tests persist of valid brew"""
        brew = Brew.objects.get(name="Brew 1")
        self.assertEqual(brew.description, "This is Brew 1")
        self.assertEqual(brew.style, "Saison")
        self.assertEqual(brew.type, "Extract")
        self.assertEqual(brew.abv, 5)
        self.assertEqual(brew.brewer.user.username, "username1")
