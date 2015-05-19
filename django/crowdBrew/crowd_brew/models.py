from django.db import models
from authentication.models import Account
from authentication.models import AccountManager

class Entity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = Account
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = Account

    class Meta:
        abstract = True

class Brewery(Entity):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    def __str__(self):
        return self.name

class Brewer(models.Model):
    brewery = models.ForeignKey(Brewery, related_name='brewers')
    user = models.OneToOneField(Account, primary_key=False)
    def __str__(self):
        return ' @ '.join((self.user.username, self.brewery.name))

class Brew(Entity):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    style = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    abv = models.IntegerField(default=0)
    brewer = models.ForeignKey(Brewer)
    def __str__(self):
        return self.name

class Image(Entity):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='/static/images/%Y/%m')
    brew = models.ForeignKey(Brew, related_name='images', null=True, blank=True)
    brewery = models.ForeignKey(Brewery, related_name='images', null=True, blank=True)
    def __str__(self):
        return self.title

class BrewDate(models.Model):
    brew = models.ForeignKey(Brew, related_name='dates', null=True, blank=True)
    date = models.DateTimeField()
    activity = models.CharField(max_length=128)
