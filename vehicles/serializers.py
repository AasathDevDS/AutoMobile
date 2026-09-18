import re
from rest_framework import serializers
from .models import Vehicle

# serializers.py
class VehicleSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            'id', 'vehicle_number', 'brand', 'model', 'year', 
            'vehicle_type', 'other_vehicle_type', 'current_mileage', 
            'created_at', 'updated_at', 
            'customer',        
            'customer_name'   
        ]
   

    



