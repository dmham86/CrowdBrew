from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        if not password:
            raise ValueError('Users must have a password')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9\_]{4,20}$',
            message='Username cannot contain spaces or special characters except _',
            code='invalid_username'
        ),
    ])

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    #date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    NEW = 'New'
    ACTIVE = 'Active'
    DISABLED = 'Disabled'
    ACCOUNT_STATUS_CHOICES = (
        (NEW, 'New'),
        (ACTIVE, 'Active'),
        (DISABLED, 'Disabled'),
    )
    account_status = models.CharField(max_length = 10,
                                      choices = ACCOUNT_STATUS_CHOICES,
                                      default = NEW)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def clean(self):
        if self.password is None or len(self.password) < 4 or len(self.password) > 40:
            raise ValidationError("Password must be between 4 and 40 characters")

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_active(self):
        return self.account_status == self.ACTIVE

    @property
    def is_unactivated(self):
        return self.account_status == self.NEW

    @is_active.setter
    def is_active(self, value):
        self.account_status = self.NEW

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_perms(self, perm_list, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def date_joined(self):
        return self.created_at

    #@date_joined.setter
    #def date_joined(self, value):
    #    self.created_at = value
