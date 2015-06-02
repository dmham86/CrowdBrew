from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import permissions, viewsets, filters
from rest_framework.response import Response

import pdb

from .serializers import *
from .models import *
from authentication.permissions import *
from .permissions import IsBrewOwner

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
    search_fields = ('name', 'description')

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