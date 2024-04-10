from django.urls import path, include
from .views import CarViewset



urlpatterns = [
    
    path('cars/', CarViewset.as_view()),
    path('cars/<int:id>', CarViewset.as_view())
    
]