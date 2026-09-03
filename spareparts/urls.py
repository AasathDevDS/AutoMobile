from django.urls import path
from .views import SparePartAPIView, DetailSparePartAPIView

urlpatterns = [
    path('', SparePartAPIView.as_view(), name='sparepart-list'),
    path('<int:pk>/', DetailSparePartAPIView.as_view(), name='sparepart-detail')
    ]