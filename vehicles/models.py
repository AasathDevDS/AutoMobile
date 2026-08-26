from django.db import models

from customer.models import Customer


class Vehicle(models.Model):

    class VehicleType(models.TextChoices):
        CAR = "CAR", "Car"
        VAN = "VAN", "Van"
        MOTORCYCLE = "MOTORCYCLE", "Motorcycle"
        THREEWHEELER = "THREEWHEELER", "Three Wheeler"
        SUV = "SUV", "SUV"
        OTHERS = 'OTHERS','Others'

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="vehicles"
    )

    vehicle_number = models.CharField(
        max_length=20,
        unique=True
    )

    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=45)
    year = models.PositiveIntegerField()

    vehicle_type = models.CharField(
        max_length=15,
        choices=VehicleType.choices,
        default=VehicleType.MOTORCYCLE,
        db_index=True
    )

    other_vehicle_type = models.CharField(
      max_length=40,
      blank=True
    )

    current_mileage = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.vehicle_number} - "
            f"{self.brand} {self.model}"
        )