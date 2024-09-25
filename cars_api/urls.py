from django.urls import path
from cars_api.views import ListCarsApiView, RetrieveUpdateDestroyCarView

urlpatterns = [
    path('cars/', ListCarsApiView.as_view()),
    path('cars/<int:pk>/',RetrieveUpdateDestroyCarView.as_view()),
]
