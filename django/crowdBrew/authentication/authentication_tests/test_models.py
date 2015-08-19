from django.test import TestCase
from authentication.models import Account
from django.core.exceptions import ValidationError

class AccountTestCase(TestCase):
    validAccount = None

    def setUp(self):
        self.validAccount = Account(email="user1@test.com",username="username1",first_name="First", last_name="Last", tagline="The First User", password="password")

    def assertValidationFail(self, item):
        with self.assertRaises(ValidationError):
            item.full_clean()
            item.save()

    def test_account_persist(self):
        """Tests validation and persist of valid account"""
        self.validAccount.full_clean()
        self.validAccount.save()

        account = Account.objects.get(username="username1")
        self.assertEqual(account.email, "user1@test.com")
        self.assertEqual(account.first_name, "First")
        self.assertEqual(account.last_name, "Last")
        self.assertEqual(account.get_full_name(), "First Last")
        self.assertEqual(account.tagline, "The First User")

    def test_username_validation(self):
        # Confirm we're starting with a valid account
        self.validAccount.full_clean()

        # underscore is only special char allowed in username
        self.validAccount.username="VALID_username"
        self.validAccount.full_clean()

        # Now for the invalid options
        invalidAccount = self.validAccount
        invalidAccount.username="Invalid username with spaces" # No whitespace
        self.assertValidationFail(invalidAccount)

        invalidAccount.username="InvalidUsernameTooLong" # More than 20 chars
        self.assertValidationFail(invalidAccount)

        invalidAccount.username="Inv@lidUsername" # No special chars except _
        self.assertValidationFail(invalidAccount)

        invalidAccount.username="no" # Username must be at least 4 chars
        self.assertValidationFail(invalidAccount)

        invalidAccount.username=None # Username must be present
        self.assertValidationFail(invalidAccount)

    def test_email_validation(self):
        # Confirm we're starting with a valid account
        self.validAccount.full_clean()

        # Test validation of account with invalid email
        # We won't test much here because we're using Django EmailField
        # and we'll trust it works
        invalidAccount = self.validAccount
        invalidAccount.email="notAnEmailAddress"
        self.assertValidationFail(invalidAccount)

        # Confirm email is not blank
        invalidAccount.email=None
        self.assertValidationFail(invalidAccount)

    def test_password_validation(self):
        # Confirm we're starting with a valid account
        self.validAccount.full_clean()

        # Test validation of account with invalid password
        invalidAccount = self.validAccount
        invalidAccount.password=None
        self.assertValidationFail(invalidAccount)

        invalidAccount.password="abc"
        self.assertValidationFail(invalidAccount)
