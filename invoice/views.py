from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
