from django.db import models

class ServiceSpareParts(models.Model):
    service = models.ForeignKey(
        'service.Service',
        on_delete=models.CASCADE,
        related_name='spare_parts'
    )
    spare_part = models.ForeignKey(
        'spareparts.SparePart',
        on_delete=models.CASCADE,
        related_name='service_spare_parts'
    )
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.spare_part_name} for Service ID: {self.service.id}"