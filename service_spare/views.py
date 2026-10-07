from rest_framework import viewsets
from .serializers import ServiceSparePartsSerializer
from .models import ServiceSpareParts

class ServiceSparePartsViewSet(viewsets.ModelViewSet):
    queryset = ServiceSpareParts.objects.all()
    serializer_class = ServiceSparePartsSerializer
    