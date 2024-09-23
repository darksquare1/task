from django import forms
from django.core.exceptions import ValidationError

from cars.models import Comment, Car
from datetime import datetime


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CarAddForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']

    def clean_year(self): # валидация, чтобы год не был больше текущего
        year = self.cleaned_data['year']
        if isinstance(year, int):
            cur_year = datetime.now().year
            if year > cur_year:
                raise ValidationError('Введите корректный год выпуска')
        return year
