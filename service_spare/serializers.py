from rest_framework import serializers
from django.db import transaction

from .models import ServiceSpareParts


class ServiceSparePartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceSpareParts
        fields = '__all__'

    def create(self, validated_data):

        with transaction.atomic():

            spare_part = validated_data['spare_part_name']
            used_quantity = validated_data['quantity']

            # Check stock
            if spare_part.quantity < used_quantity:
                raise serializers.ValidationError(
                    f"Only {spare_part.quantity} items available in stock."
                )

            # Reduce stock
            spare_part.quantity -= used_quantity
            spare_part.save()

            # Create ServiceSpareParts record
            service_spare = ServiceSpareParts.objects.create(
                **validated_data
            )

            return service_spare