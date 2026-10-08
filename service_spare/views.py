from rest_framework import viewsets
from .serializers import ServiceSparePartsSerializer
from .models import ServiceSpareParts
from rest_framework.permissions import IsAuthenticated

class ServiceSparePartsViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]  
    queryset = ServiceSpareParts.objects.all()
    serializer_class = ServiceSparePartsSerializer

    