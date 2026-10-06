from django.urls import path
from .views import ServiceAPIView, DetailServiceAPIView

urlpatterns = [
  path('' , ServiceAPIView.as_view() , name='service-list'),
  path('<int:pk>/' , DetailServiceAPIView.as_view() , name='service-detail'),
]