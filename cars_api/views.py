from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from cars.models import Car
from cars_api.serializers import CarSerializer


class ListCarsApiView(generics.ListAPIView):
    """
    Представление для отображения машин в json по get запросу
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class RetrieveUpdateDestroyCarView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения конкретной машины, обновления и удаления (get, put, delete) соответственно
    """
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def put(self, request, *args, **kwargs):
        if request.user != self.get_object().owner: # если запрос делает не владелец записи, то отвечаем запретом
            return Response({'detail': 'Вы не создатель данной записи'}, status=403)
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if request.user != self.get_object().owner: # если запрос делает не владелец записи, то отвечаем запретом
            return Response({'detail': 'Вы не создатель данной записи'}, status=403)
        return super().delete(request, *args, **kwargs)
