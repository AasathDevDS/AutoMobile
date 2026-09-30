from rest_framework import serializers
# from .models import Service
from spareparts.models import SparePart
from service.models import Service

class LowStockAlert(serializers.ModelSerializer):
  class Meta:
    model = SparePart
    fields = [
      'name',
      'quantity',
      'minimum_stock',
      'unit_price'

    ]




class RecentServiceSerializer(serializers.ModelSerializer):
    # Foreign key relations-ல் இருந்து குறிப்பிட்ட data-வை மட்டும் எடுக்க:
    reg_no = serializers.CharField(source='vehicle.vehicle_number', read_only=True)
    vehicle_model = serializers.CharField(source='vehicle.model', read_only=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Service
        fields = [
            'id',
            'reg_no',
            'vehicle_model',
            'customer_name',
            'status',
            'created_at',
        ]