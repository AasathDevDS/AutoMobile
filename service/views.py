from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .models import Service
from .serializers import ServiceSerializer

# Create your views here.
class ServiceAPIView(APIView):
  def get(self, request):
    search = request.query_params.get("search", "").strip()

    services = Service.objects.select_related(
        "vehicle",
        "mechanic"
    ).all()

    if search:
        services = services.filter(
            Q(vehicle__vehicle_number__icontains=search) |
            Q(mechanic__name__icontains=search) |
            Q(service_type__icontains=search) |
            Q(status__icontains=search)
        )

    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)
  
  def post(self,request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailServiceAPIView(APIView):
  
  def get_object(self,pk):
    return get_object_or_404(Service, pk=pk)
  
  def get(self,request,pk):
    service = self.get_object(pk)
    serializer = ServiceSerializer(service)
    return Response(serializer.data , status=status.HTTP_200_OK)

  def put(self,request,pk):
    service = self.get_object(pk)
    serializer = ServiceSerializer(service, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self,request,pk):
    service = self.get_object(pk)
    serializer = ServiceSerializer(service, data=request.data , partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,pk):
    service = self.get_object(pk)
    service.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)