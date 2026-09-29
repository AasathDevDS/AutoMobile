from decimal import Decimal
from rest_framework import serializers
from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    vehicle_number = serializers.ReadOnlyField(source='service.vehicle.vehicle_number')
    vehicle_model = serializers.ReadOnlyField(source='service.vehicle.model')
    vehicle_brand = serializers.ReadOnlyField(source='service.vehicle.brand')

    class Meta:
        model = Invoice
        fields = [
            'id',
            'invoice_date',
            'service_charge',
            'parts_cost',
            'discount',
            'total_amount',
            'paid_amount',
            'remaining_amount',
            'payment_status',
            'payment_method',
            'notes',
            'service',          
            'vehicle_number',   
            'vehicle_model',
            'vehicle_brand',
        ]

        read_only_fields = [
            "total_amount",
            "remaining_amount"
        ]

    def validate(self, attrs):
        instance = self.instance

        # Partial update (PATCH) மற்றும் Create இரண்டிற்கும் fallback handling
        service_charge = attrs.get(
            "service_charge",
            instance.service_charge if instance else Decimal("0.00")
        )

        parts_cost = attrs.get(
            "parts_cost",
            instance.parts_cost if instance else Decimal("0.00")
        )

        discount = attrs.get(
            "discount",
            instance.discount if instance else Decimal("0.00")
        )

        paid_amount = attrs.get(
            "paid_amount",
            instance.paid_amount if instance else Decimal("0.00")
        )

        payment_status = attrs.get(
            "payment_status",
            instance.payment_status
            if instance
            else Invoice.PaymentStatus.PENDING
        )

        payment_method = attrs.get(
            "payment_method",
            instance.payment_method if instance else None
        )

        # 1. Negative Checks
        if service_charge < 0:
            raise serializers.ValidationError({
                "service_charge": "Service charge cannot be negative."
            })

        if parts_cost < 0:
            raise serializers.ValidationError({
                "parts_cost": "Parts cost cannot be negative."
            })

        if discount < 0:
            raise serializers.ValidationError({
                "discount": "Discount cannot be negative."
            })

        if paid_amount < 0:
            raise serializers.ValidationError({
                "paid_amount": "Paid amount cannot be negative."
            })

        # 2. Total Calculation
        subtotal = service_charge + parts_cost

        if subtotal <= 0:
            raise serializers.ValidationError({
                "service_charge": "Service charge or parts cost must be greater than zero."
            })

        if discount > subtotal:
            raise serializers.ValidationError({
                "discount": "Discount cannot exceed the subtotal."
            })

        total_amount = subtotal - discount
        remaining_amount = total_amount - paid_amount

        if paid_amount > total_amount:
            raise serializers.ValidationError({
                "paid_amount": "Paid amount cannot exceed the total amount."
            })

        # 3. Payment Status Validations
        if payment_status == Invoice.PaymentStatus.PENDING:
            if paid_amount != Decimal("0.00"):
                raise serializers.ValidationError({
                    "paid_amount": "Pending invoices must have a paid amount of zero."
                })
            attrs["payment_method"] = None

        elif payment_status == Invoice.PaymentStatus.PARTIALLY_PAID:
            if paid_amount <= Decimal("0.00"):
                raise serializers.ValidationError({
                    "paid_amount": "Paid amount must be greater than zero."
                })
            if paid_amount >= total_amount:
                raise serializers.ValidationError({
                    "paid_amount": "Partial payment must be less than the total amount."
                })
            if not payment_method:
                raise serializers.ValidationError({
                    "payment_method": "Payment method is required."
                })

        elif payment_status == Invoice.PaymentStatus.PAID:
            if paid_amount != total_amount:
                raise serializers.ValidationError({
                    "paid_amount": "Paid amount must equal the total amount."
                })
            if not payment_method:
                raise serializers.ValidationError({
                    "payment_method": "Payment method is required."
                })

        elif payment_status == Invoice.PaymentStatus.CANCELLED:
            paid_amount = Decimal("0.00")
            attrs["paid_amount"] = paid_amount
            attrs["payment_method"] = None
            remaining_amount = Decimal("0.00")

        # கணக்கிடப்பட்ட மதிப்புகளை validated data-வுக்குள் inject செய்தல்
        # இதன் மூலம் Model instance-க்கு சரியான calculated values கிடைக்கும்
        attrs["total_amount"] = total_amount
        attrs["remaining_amount"] = remaining_amount

        return attrs