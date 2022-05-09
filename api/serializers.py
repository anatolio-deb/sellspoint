from django.forms import FloatField
from rest_framework import serializers

class SellsPointSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    pk = serializers.IntegerField()

class VisitSerializer(serializers.Serializer):
    time = serializers.DateTimeField()
    visits = serializers.PrimaryKeyRelatedField(read_only=True)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    pk = serializers.IntegerField()