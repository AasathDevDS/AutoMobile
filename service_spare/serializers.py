from rest_framework import serializers
from .models import ServiceSpareParts

class ServiceSparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSpareParts
        fields = '__all__'
