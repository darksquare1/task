from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserRegisterSerializer


class SignUpView(CreateView):
    """
    Класс для создания нового пользователя
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class SignUpApiView(CreateAPIView):
    """
    Класс для создания нового пользователя по api
    """
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class LoginApiView(APIView):
    """
    Класс для авторизации пользователя по апи
    """

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Вы успешно вошли'}, status=200)
        else:
            return Response({'error': 'Неверное имя пользователя или пароль'}, status=400)


class LogoutApiView(APIView):
    """
    Класс для выхода из аккаунта через апи
    """
    permission_classes = [IsAuthenticated] # допускаем выход только авторизированным пользователям

    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=200)
