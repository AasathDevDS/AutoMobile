from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = '__all__'
    read_only_fields = ["id" , "created_at"]

    def validate_phone(self, value):
      cleaned_phone = value.replace(" ","")

      if not cleaned_phone.isdigit():
        raise serializers.ValidationError(
          "Phone number must contain only digits.")
      
      if len(cleaned_phone) != 10:
        raise serializers.ValidationError(
                "Phone number must contain 10 digits."
            ) 
      return cleaned_phone


  
