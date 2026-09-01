from django.db import models
from django.utils import timezone


class Service(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    vehicle = models.ForeignKey(
        "vehicles.Vehicle",
        related_name="services",
        on_delete=models.PROTECT
    )

    mechanic = models.ForeignKey(
        "mechanics.Mechanic",
        related_name="services",
        on_delete=models.PROTECT
    )

    service_date = models.DateTimeField(default=timezone.now)

    service_type = models.CharField(max_length=100)

    problem_description = models.TextField()

    mileage_at_service = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    estimated_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    actual_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    notes = models.TextField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.vehicle} - "
            f"{self.service_type} - "
            f"{self.get_status_display()}"
        )