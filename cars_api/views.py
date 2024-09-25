from rest_framework import generics
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response

from cars.models import Car, Comment
from cars_api.serializers import CarSerializer, CommentSerializer


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
        if request.user != self.get_object().owner:  # если запрос делает не владелец записи, то отвечаем запретом
            return Response({'detail': 'Вы не создатель данной записи'}, status=403)
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if request.user != self.get_object().owner:  # если запрос делает не владелец записи, то отвечаем запретом
            return Response({'detail': 'Вы не создатель данной записи'}, status=403)
        return super().delete(request, *args, **kwargs)


class GetAddCommentsApiView(ListAPIView):
    """
    Класс для просмотра и добавления комментариев по апи
    """
    serializer_class = CommentSerializer

    def get_queryset(self): # переопределяем метод для получения комментариев только к определенной записи
        pk = self.kwargs['pk'] # берем айди машины из строки url
        car = get_object_or_404(Car, pk=pk) # получаем машину либо если ее нет возвращаем 404
        return Comment.objects.filter(car=car)

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated: # если комментирует не авторизированный пользователь, то возвращаем ошибку
            return Response({'error': 'Вы не авторизованы и не можете добавлять комментарии'}, status=401)
        pk = self.kwargs['pk'] # получаем айди машины из строки url
        car = get_object_or_404(Car, pk=pk) # берем айди машины из строки url
        serializer = CommentSerializer(data=request.data) # десереализиуем данные
        if serializer.is_valid():
            serializer.save(car=car, author=user) # сохраняем комментарий если он валидный
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) # возвращаем ошибки если данные не валидны
