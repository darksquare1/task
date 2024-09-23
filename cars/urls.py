from django.urls import path
from cars.views import CarListView

urlpatterns = [
    path('', CarListView.as_view(), name='index'),
]