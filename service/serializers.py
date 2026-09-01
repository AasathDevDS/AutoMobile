from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = "__all__"

    # def validate_service_date(self,value):
    #   if value < timezone.now():
    #     raise serializers.ValidationError(
    #       "Service date cannot be in the past."
    #     )
    #     return value

    def validate_mileage_at_service(self,value):
      if value < 0:
        raise serializers.ValidationError(
          "Mileage at service cannot be negative."
        )
      return value
    
    def validate_mechanic(self,value):
      if not value.is_active:
        raise serializers.ValidationError(
          "Mechanic is not active."
        )
      return value

