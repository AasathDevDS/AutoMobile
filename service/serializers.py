from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    # 'vehicle' என்ற Foreign Key வழியே நேரடி navigation
    vehicle_number = serializers.ReadOnlyField(source='vehicle.vehicle_number')
    vehicle_model = serializers.ReadOnlyField(source='vehicle.model')
    vehicle_brand = serializers.ReadOnlyField(source='vehicle.brand')

    mechanic_name = serializers.CharField(source='mechanic.name', read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 
            'vehicle',           # POST / PUT-க்கு Vehicle ID (e.g. 1)
            'vehicle_number',    # Frontend display (e.g. "BCC-8430")
            'vehicle_model',     # Frontend display (e.g. "Civic")
            'vehicle_brand',     # Frontend display (e.g. "Honda")
            'mechanic',          # Mechanic ID
            'mechanic_name',     # Frontend display
            'service_type',
            'service_date',
            'status',
            'estimated_cost',
            'actual_cost',
            'mileage_at_service',
            'problem_description',
            'notes',
            'created_at',
            'updated_at'
        ]