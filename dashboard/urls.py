from django.urls import path
from .views import DashboardSummaryView

urlpatterns = [
    # Dashboard Overview Endpoint
    path('', DashboardSummaryView.as_view(), name='dashboard-summary'),
]