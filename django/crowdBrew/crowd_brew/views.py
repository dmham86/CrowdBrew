from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, viewsets

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
    queryset = Brew.objects.order_by('-id')
    serializer_class = BrewSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsBrewOwner(),)

    def perform_create(self, serializer):
        instance = serializer.save(brewer=self.request.user.brewer)

        return super(BrewViewSet, self).perform_create(serializer)
