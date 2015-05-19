from django.conf.urls import url, include, patterns
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from . import views
from authentication.views import AccountSerializer
from .models import *
from .serializers import *

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from authentication.views import AccountViewSet, IndexView, LoginView, LogoutView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'brewer', views.BrewerViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'brews', views.BrewViewSet)

urlpatterns = patterns(
    '',

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url('^.*$', IndexView.as_view(), name='index'),
)
