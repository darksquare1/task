from django.shortcuts import render
from rest_framework import generics
from cars.models import Car
from cars_api.serializers import CarSerializer


class ListCarsApiView(generics.ListAPIView): # представление для отображения машин в json по гет запросу
    queryset = Car.objects.all()
    serializer_class = CarSerializer

