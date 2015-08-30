from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.models import Site, RequestSite
from django.conf import settings

import json

from registration import signals
from registration.models import RegistrationProfile
from registration.views import ActivationView as BaseActivationView
from registration.views import RegistrationView as BaseRegistrationView
from registration.users import UserModel

class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    SEND_ACTIVATION_EMAIL = getattr(settings, 'SEND_ACTIVATION_EMAIL', True)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if Site._meta.installed:
                site = Site.objects.get_current()
            else:
                site = RequestSite(request)

            new_user_instance = UserModel().objects.create_user(**serializer.validated_data)

            new_user = RegistrationProfile.objects.create_inactive_user(
                new_user=new_user_instance,
                site=site,
                send_email=self.SEND_ACTIVATION_EMAIL,
                request=request,
            )
            signals.user_registered.send(sender=self.__class__,
                                         user=new_user,
                                         request=request)

            new_user_serializer = self.serializer_class(new_user)

            return Response(new_user_serializer.data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)
    def post(self, request, format=None):

        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is None:
            try:
                user = Account.objects.get(username=email)
                account = authenticate(email=user.email, password=password)
            except Account.DoesNotExist:
                account = None;

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            if account.is_unactivated:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has not been activated. Check your email for an activation link.'
                }, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            'status': 'Unauthorized',
            'message': 'Username/password combination invalid.'
        }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
