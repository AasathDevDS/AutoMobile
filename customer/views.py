from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer


# Create your views here.
class CustomerApiView(APIView):
  def get(self, request):
    customers = Customer.objects.all()

    name = request.query_params.get('name')
    phone = request.query_params.get('phone')

    if name:
      customers = customers.filter(name__icontains=name)
    if phone:
      customers = customers.filter(phone__icontains=phone)

    serializer = CustomerSerializer(customers , many =True)
    
    return Response(serializer.data , status=status.HTTP_200_OK)


  def post(self , request ):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomerDetailApiView(APIView):

  def get_object(self,pk):
    return get_object_or_404(Customer,pk=pk)

  def get(self, request, pk):
    customer = self.get_object(pk)
    serializer = CustomerSerializer(customer)

    return Response(serializer.data , status = status.HTTP_200_OK)

  def put(self, request, pk):
    customer = self.get_object(pk)
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self,request,pk):
    customer = self.get_object(pk)
    serializer = CustomerSerializer(customer , data=request.data , partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data , status = status.HTTP_200_OK)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,pk):
    customer = self.get_object(pk)
    customer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




