
from rest_framework import serializers
from .models import Test
class TestSerializer(serializers.Serializer):
    class Meta:
        model = Test
        fields = ['name','lastName']