from django.db import models

# Create your models here.
class Mechanic(models.Model):
  name = models.CharField(max_length=64)
  phone = models.CharField(max_length=12 , db_index=True)
  specialization = models.CharField(max_length=256)
  is_available = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.name
  