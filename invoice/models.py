from decimal import Decimal
from django.db import models
from django.utils import timezone


class Invoice(models.Model):

    class PaymentMethod(models.TextChoices):
        CASH = "CASH", "Cash"
        CARD = "CARD", "Card"
        BANK_TRANSFER = "BANK_TRANSFER", "Bank Transfer"
        ONLINE_PAYMENT = "ONLINE_PAYMENT", "Online Payment"

    class PaymentStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PARTIALLY_PAID = "PARTIALLY_PAID", "Partially Paid"
        PAID = "PAID", "Paid"
        CANCELLED = "CANCELLED", "Cancelled"

    service = models.OneToOneField(
        "service.Service",
        on_delete=models.PROTECT,
        related_name="invoice"
    )

    invoice_date = models.DateTimeField(
        default=timezone.now
    )

    service_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00")
    )

    parts_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00")
    )

    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00")
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        editable=False
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00")
    )

    remaining_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        editable=False
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    def calculate_amounts(self):
        total = (
            self.service_charge
            + self.parts_cost
            - self.discount
        )

        self.total_amount = max(
            Decimal("0.00"),
            total
        )

        self.remaining_amount = max(
            Decimal("0.00"),
            self.total_amount - self.paid_amount
        )

    def save(self, *args, **kwargs):
        self.calculate_amounts()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice #{self.id} - Service #{self.service_id}"