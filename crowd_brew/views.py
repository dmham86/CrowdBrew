from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json

from rest_framework import permissions, viewsets, filters, status
from rest_framework.response import Response

import pdb
import logging

from .serializers import *
from .models import *
from authentication.permissions import *
from authentication.models import Account
from authentication.serializers import AccountSerializer
from authentication.views import AccountViewSet
from .permissions import IsBrewOwner

logger = logging.getLogger("crowd_brew.views")

class BreweryViewSet(viewsets.ModelViewSet):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer


class BrewerViewSet(viewsets.ModelViewSet):
    queryset = Brewer.objects.all()
    serializer_class = BrewerSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsBrewer(),)

class BrewViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = BrewSerializer
    queryset = Brew.objects.order_by('-id')
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'description', 'brewer__user__username', 'brewer__brewery__name']

    #def get_queryset(self):
        #queryset = Brew.objects.order_by('-id')
        #searchName = self.request.query_params.get('search', None)
        #if searchName is not None:
        #    queryset = queryset.filter(name__contains=searchName)
        #return queryset

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsBrewOwner(),)

    def perform_create(self, serializer):
        instance = serializer.save(brewer=self.request.user.brewer)

        return super(BrewViewSet, self).perform_create(serializer)

class AccountBrewsViewSet(viewsets.ModelViewSet):
    queryset = Brew.objects.select_related('brewer').all()
    serializer_class = BrewSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (IsAccountOwner(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(brewer__user__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

class TastingViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tasting.objects.order_by('-id')
    serializer_class = TastingSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsBrewOwner(),)

    def perform_create(self, serializer):
        #pdb.set_trace()
        instance = serializer.save(user=self.request.user, brew=Brew.objects.get(id=self.request.data['brew_id']))

        return super(TastingViewSet, self).perform_create(serializer)

class RegistrationViewSet(viewsets.ModelViewSet):
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
        registrationResponse = AccountViewSet().create(request=request)
        account_data = registrationResponse.data
        if registrationResponse.status_code == status.HTTP_201_CREATED and request.data['account_type'] == "Brewer":
            logger.debug(request.data['account_type'])
            logger.debug(request.data['brewery_name'])
            brewery_data = {"name" : request.data['brewery_name'], "description": ""}
            logger.debug(brewery_data)
            brewery_serializer = BrewerySerializer(data=brewery_data)
            brewery_instance = {}
            if brewery_serializer.is_valid():
                #TODO: Create brewery and brewer
                brewery_instance = brewery_serializer.save()
                brewer = Brewer.objects.create(user=Account.objects.get(id=account_data['id']), brewery=brewery_instance)
                return Response({"account": account_data, "brewer": BrewerSerializer(brewer).data}, status.HTTP_201_CREATED)
            return Response({"account": account_data, "brewery": brewery_serializer.data}, status.HTTP_201_CREATED)
        return registrationResponse
