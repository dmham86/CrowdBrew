from django.contrib.auth import update_session_auth_hash
from django_gravatar.helpers import get_gravatar_url

from rest_framework import serializers

from authentication.models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    gravatar_url = serializers.SerializerMethodField('get_gravatar')

    def get_gravatar(self, account):
        return get_gravatar_url(account.email)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'account_type',
                  'first_name', 'last_name', 'tagline', 'password',
                  'confirm_password', 'is_admin', 'gravatar_url')
        read_only_fields = ('is_admin', 'gravatar_url')

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.tagline = validated_data.get('tagline', instance.tagline)

        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)

        return instance
