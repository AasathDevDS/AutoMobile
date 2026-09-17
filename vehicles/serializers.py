import re
from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

        read_only_fields = [
            "id",
            # "customer_name",
            "created_at",
            "updated_at",
        ]
   

    



