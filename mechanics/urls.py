from django.urls import path,include
from .views import MechanicAPIView,MechanicDetailView


urlpatterns = [
  path("" , MechanicAPIView.as_view()),
  path("<int:pk>/", MechanicDetailView.as_view())
]