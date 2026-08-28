from rest_framework import serializers
from .models import Mechanic


class MechanicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mechanic
    fields = [
      "name",
      "phone",
      "specialization",
      "is_available",
      "created_at",
      "updated_at"
    ]

    def validate_phone(self,value):
      cleaned_phone = value.replace(" ", "")
      if not cleaned_phone.isdigit():
        raise serializers.ValidationError("Please Enter Phone Number in digits.Please Check Phone Number .....")
      if len(cleaned_phone) != 10:
        raise serializers.ValidationError("Your Phone Number contains more than 10 characters.Add a valid Number")
      
      return cleaned_phone

