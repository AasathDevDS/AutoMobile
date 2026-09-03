from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import SparePart
from .serializers import SparePartSerializer


class SparePartAPIView(APIView):

    def get(self, request):
        search = request.query_params.get("search", "").strip()
        lowstock = request.query_params.get("lowstock", "")
        

        spareparts = SparePart.objects.all()

        if search:
            spareparts = spareparts.filter(
                Q(name__icontains=search) |
                Q(category__icontains=search) |
                Q(supplier__icontains=search) 
            )

        if lowstock=="true":
            spareparts = spareparts.filter(
              quantity__lte=F("minimum_stock")
            ) 

        serializer = SparePartSerializer(spareparts, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = SparePartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DetailSparePartAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(SparePart, pk=pk)


    def get(self, request, pk):
        spare_part = self.get_object(pk)

        serializer = SparePartSerializer(spare_part)

        return Response(serializer.data)


    def put(self, request, pk):
        spare_part = self.get_object(pk)

        serializer = SparePartSerializer(
            spare_part,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def patch(self, request, pk):
        spare_part = self.get_object(pk)

        serializer = SparePartSerializer(
            spare_part,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def delete(self, request, pk):
        spare_part = self.get_object(pk)

        spare_part.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )