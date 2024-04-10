from rest_framework import serializers
from .models import Cars


class CarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        
        fields = ['car_name', 'car_version', 'car_model', 'car_price']