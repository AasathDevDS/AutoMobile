import re
from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
        source="customer.name",
        read_only=True
    )

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "customer_name",
            "vehicle_number",
            "brand",
            "model",
            "year",
            "vehicle_type",
            "current_mileage",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "customer_name",
            "created_at",
            "updated_at",
        ]
    def validate_vehicle_number(self, value):
      value = value.strip().upper()
      pattern = r"^[A-Z]{2,3}-d{4}$"
      if not re.fullmatch(pattern,value):
        raise serializers.ValidationError(
          "Vehicle number must be in the format BCC-8430."
        )
      return value

    def validate_year(self,value):
      current_year = day.today().year
      
      if value<1886:
        raise serializers.ValidationError(
          "Manufacturing year cannot be before 1886."
        )
      if current_year < value:
        raise serializers.ValidationError(
          "Manufacturing year cannot be in future."
        )
      return value

    def validate_current_mileage(self,value):
      if value > 200000:
        raise serializers.ValidationError(
          "Invalid Mileage"
        )
      return value

    



