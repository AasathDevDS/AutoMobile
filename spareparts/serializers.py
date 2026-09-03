from rest_framework import serializers
from .models import SparePart

class SparePartSerializer(serializers.ModelSerializer):
  class Meta:
    model = SparePart
    fields = [
      'id',
      'name',
      'category',
      'supplier',
      'quantity',
      'minimum_stock',
      'unit_price',
      'created_at',
      'updated_at'
    ]
    read_only_fields = [
      'id',
      'created_at'
    ]

  def validate_quantity(self, value):
      if value < 0:
          raise serializers.ValidationError("Quantity cannot be negative.")
      return value

  def validate_unit_price(self, value):
      if value < 0:
          raise serializers.ValidationError("Unit price cannot be negative.")
      return value