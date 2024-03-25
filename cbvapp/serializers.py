from rest_framework import serializers
from .models import Cars

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        # fields = ['brand','year','type']
        fields = '__all__'
    