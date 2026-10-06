from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceAPIView, DetailServiceAPIView, ServiceSparePartViewSet

router = DefaultRouter()
# Router-ல் prefix வெறுமனே 'items' அல்லது 'parts' என்று வையுங்கள்:
router.register(r'parts', ServiceSparePartViewSet, basename='service-spare-part')

urlpatterns = [
    # Router endpoints (e.g., /services/spare-parts/...)
    path('spare-parts/', include(router.urls)),

    # Service endpoints
    path('', ServiceAPIView.as_view(), name='service-list'),
    path('<int:pk>/', DetailServiceAPIView.as_view(), name='service-detail'),
]