from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet
from django.urls import path,include

router = DefaultRouter()
router.register(r"", VehicleViewSet , basename="vehicles")

urlpatterns = [
    path('', include(router.urls)),
]
