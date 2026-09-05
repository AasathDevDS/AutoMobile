from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer
# Create your views here.

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
