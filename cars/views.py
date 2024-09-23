from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from cars.forms import CommentForm
from cars.models import Car, Comment


class CarListView(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'cars/car_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(car=self.get_object()) # находим все коментарии, принадлежащие машине
        context['comments'] = comments # добавляем их в контекст для использования в шаблоне
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(data=request.POST)
        self.object = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = self.object # устанавливаем машину к которой пренадлежит комментарий
            comment.author = self.request.user # устанавливаем пользователя который создал комментарий
            comment.save()
        self.extra_context = {'form': form} # добавляем форму в контекст
        return super().render_to_response(self.get_context_data())

    def get(self, request, *args, **kwargs):
        initial = {}
        self.extra_context = {'form': CommentForm(initial=initial)} # добавляем пустую форму в контекст
        return super().get(request, *args, **kwargs)


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('index')
    template_name = 'cars/car_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        car = self.get_object() # получаем объект машины
        if car.owner == request.user: # смотрим чтобы удалять мог только тот, кто создал запись
            messages.success(request, "Автомобиль успешно удалён.")
            return super().delete(request, *args, **kwargs)
        else:
            messages.error(request, "У вас нет прав на удаление этого автомобиля.")
            return redirect('index')
