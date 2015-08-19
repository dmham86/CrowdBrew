from django.test import TestCase
from django.core.exceptions import ValidationError
from authentication.models import Account
from crowd_brew.models import *

class BrewTestCase(TestCase):
    brewerAccount = Account(email="user1@test.com",username="username1",first_name="First", last_name="Last", tagline="The First User", password="password")
    tastingAccount = Account(email="user2@test.com",username="username2",first_name="Test", last_name="User", tagline="Another User", password="supersecret")
    brewery1 = Brewery(name="Brewery 1", description="Some information about Brewery 1")
    brewer1 = None
    firstBrew = None

    def setUp(self):
        self.persist_valid_models()


    def assertValidationFail(self, item):
        with self.assertRaises(ValidationError):
            item.full_clean()
            item.save()

    def persist_valid_models(self):
        self.brewerAccount.full_clean()
        self.brewerAccount.save()
        self.tastingAccount.full_clean()
        self.tastingAccount.save()

        self.brewery1.full_clean()
        self.brewery1.save()

        self.brewer1 = Brewer(user=self.brewerAccount, brewery=self.brewery1)
        self.brewer1.full_clean()
        self.brewer1.save()

        self.firstBrew = Brew(name="Brew 1", description="This is Brew 1", style="Saison", type="Extract", abv=5, brewer=self.brewer1)
        self.firstBrew.full_clean()
        self.firstBrew.save()

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

    def test_tasting_persist(self):
        """Test persist of valid tasting"""
        expectedTasting = Tasting(brew=self.firstBrew, user=self.tastingAccount, appearance=5.0, smell=4.0, taste=3.5, mouthfeel=1.0, overall=4.0)
        expectedTasting.full_clean()
        expectedTasting.save()
        receivedTasting = Tasting.objects.get(brew=self.firstBrew)
        self.assertEqual(receivedTasting, expectedTasting)

    def test_tasting_validation(self):
        """Test validation of invalid tastings"""
        validTasting = Tasting(brew=self.firstBrew, user=self.tastingAccount, appearance=5.01, smell=4.0, taste=3.5, mouthfeel=1.0, overall=4.0)
        invalidTasting = validTasting
        invalidTasting.appearance = -0.001
        self.assertValidationFail(invalidTasting)
        invalidTasting.appearance = 5.001
        self.assertValidationFail(invalidTasting)

        invalidTasting = validTasting
        invalidTasting.smell = -0.001
        self.assertValidationFail(invalidTasting)
        invalidTasting.smell = 5.001
        self.assertValidationFail(invalidTasting)

        invalidTasting = validTasting
        invalidTasting.taste = -0.001
        self.assertValidationFail(invalidTasting)
        invalidTasting.taste = 5.001
        self.assertValidationFail(invalidTasting)

        invalidTasting = validTasting
        invalidTasting.mouthfeel = -0.001
        self.assertValidationFail(invalidTasting)
        invalidTasting.mouthfeel = 5.001
        self.assertValidationFail(invalidTasting)

        invalidTasting = validTasting
        invalidTasting.overall = -0.001
        self.assertValidationFail(invalidTasting)
        invalidTasting.overall = 5.001
        self.assertValidationFail(invalidTasting)

        with self.assertRaises(ValueError):
            invalidTasting = Tasting(brew=None, user=self.tastingAccount, appearance=4.0, smell=4.0, taste=3.5, mouthfeel=1.0, overall=4.0)

        with self.assertRaises(ValueError):
            invalidTasting = Tasting(brew=self.firstBrew, user=None, appearance=4.0, smell=4.0, taste=3.5, mouthfeel=1.0, overall=4.0)
