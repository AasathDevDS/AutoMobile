from django.urls import path
from .views import ServiceSparePartsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ServiceSparePartsViewSet, basename='service-spare-parts')

urlpatterns  = router.urls