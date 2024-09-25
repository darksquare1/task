from django.contrib.auth.forms import User
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор, нужный для создания нового пользователя
    """
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'Error': 'Пароли не совпадают'})
        user = User(username=self.validated_data['username'])
        user.set_password(password)
        user.save()