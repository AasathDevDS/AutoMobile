from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Mechanic
from .serializers import MechanicSerializer

# Create your views here.
class MechanicAPIView(APIView):
  def get(self,request):
    mechanics = Mechanic.objects.all()

    name = request.query_params.get('name')
    phone = request.query_params.get('phone')
    if name:
      mechanics = mechanics.filter(name__icontains=name)
    if phone:
      mechanics = mechanics.filter(phone__icontains=phone)

    serializer = MechanicSerializer(mechanics , many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)
  
  def post(self,request):
    serializer = MechanicSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


  

class MechanicDetailView(APIView):
  
  def get_object(self,pk):
    return get_object_or_404(Mechanic, pk=pk)
  
  def get(self,request,pk):
    

    mechanics = self.get_object(pk)
    serializer = MechanicSerializer(mechanics)
    return Response(serializer.data , status=status.HTTP_200_OK)

  def put(self,request,pk):
    mechanic = self.get_object(pk)
    serializer = MechanicSerializer(mechanic, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self,request,pk):
    mechanic = self.get_object(pk)
    serializer = MechanicSerializer(mechanic, data=request.data , partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,pk):
    mechanic = self.get_object(pk)
    mechanic.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


