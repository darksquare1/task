from django.urls import path
from cars_api.views import ListCarsApiView

urlpatterns = [
    path('cars/', ListCarsApiView.as_view())
]
