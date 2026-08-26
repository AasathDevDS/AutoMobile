from django.urls import path
from .views import CustomerApiView , CustomerDetailApiView

urlpatterns = [
    path('' , CustomerApiView.as_view()),
    path('<int:pk>/' , CustomerDetailApiView.as_view())
]
