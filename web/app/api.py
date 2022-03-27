import datetime
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import BaseSerializer
from app.models import Rate, BaseRate


class RateViewSet(viewsets.ModelViewSet):
    
    queryset = BaseRate.objects.all()
    serializer_class = BaseSerializer
