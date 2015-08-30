from django.dispatch import receiver
from .models import Account
from registration.signals import user_activated
import pdb

@receiver(user_activated)
def set_user_active(sender, user, request, **kwargs):
    account = Account.objects.get(id=user.id)
    if(account):
        account.account_status = Account.ACTIVE
        account.save()
