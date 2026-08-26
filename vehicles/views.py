from rest_framework import viewsets,status
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
  queryset = Vehicle.objects.all()
  serializer_class = VehicleSerializer
  

