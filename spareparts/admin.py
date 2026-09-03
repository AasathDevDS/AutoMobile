from django.contrib import admin
from .models import SparePart


# Register your models here.
list_display = ('name',  'quantity', 'minimum_stock', 'unit_price', 'updated_at')
admin.site.register(SparePart, list_display=list_display)
