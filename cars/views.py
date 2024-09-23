from django.shortcuts import render
from django.views.generic import ListView
from cars.models import Car, Comment


class CarListView(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'cars/car_list.html'

