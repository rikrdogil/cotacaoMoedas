# from django.urls import re_path

# from . import views

# urlpatterns = [
#     re_path(r'^$', views.home_app, name='home_app'),
# ]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from app import views
from app import api
from app import serializers

router = routers.DefaultRouter()
router.register(r'rates', api.RateViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.home_app, name='home_app'),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
