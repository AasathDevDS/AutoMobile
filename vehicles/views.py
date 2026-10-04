from rest_framework import viewsets,status
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.permissions import IsAuthenticated

class VehicleViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = Vehicle.objects.all()
  serializer_class = VehicleSerializer
  

