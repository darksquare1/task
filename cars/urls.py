from django.urls import path
from cars.views import CarListView, CarDetailView, CarDeleteView

urlpatterns = [
    path('', CarListView.as_view(), name='index'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]
