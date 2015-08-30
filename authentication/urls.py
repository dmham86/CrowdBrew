from django.conf.urls import url, include
from rest_framework import routers

from authentication.views import IndexView, AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    '',

    url(r'^v1/', include(router.urls)),
]
