from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Car(models.Model):
    make = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.PositiveIntegerField(verbose_name='Год выпуска', blank=True, null=True, default='Не указано')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at'])]

    def get_absolute_url(self):
        return reverse_lazy('car_detail', args=[self.pk])


class Comment(models.Model):
    content = models.TextField(verbose_name='Содержание комментария')
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at'])]
