from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rest_framework.generics import CreateAPIView
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


