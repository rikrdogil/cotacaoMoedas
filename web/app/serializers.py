from app.models import Rate,BaseRate
from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['rate', 'valor']
 
 
class BaseSerializer(serializers.ModelSerializer):
    rates = RateSerializer(many=True, read_only=True)
    class Meta:
        model = BaseRate
        fields = ['date', 'base','rates']


