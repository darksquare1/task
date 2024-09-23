from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from cars.forms import CommentForm, CarAddForm
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
        comments = Comment.objects.filter(car=self.get_object())  # находим все комментарии, принадлежащие машине
        context['comments'] = comments  # добавляем их в контекст для использования в шаблоне
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(data=request.POST)
        self.object = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = self.object  # устанавливаем машину, к которой принадлежит комментарий
            comment.author = self.request.user  # устанавливаем пользователя, который создал комментарий
            comment.save()
        self.extra_context = {'form': form}  # добавляем форму в контекст
        return self.render_to_response(self.get_context_data())  # вызываем метод, который рендерит шаблон

    def get(self, request, *args, **kwargs):
        initial = {}
        self.extra_context = {'form': CommentForm(initial=initial)}  # добавляем пустую форму в контекст
        return super().get(request, *args, **kwargs)  # вызываем метод базового класса для отображения


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('index')
    template_name = 'cars/car_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        car = self.get_object()  # получаем объект машины
        if car.owner == request.user:  # смотрим, чтобы удалять мог только тот, кто создал запись
            messages.success(request,
                             "Автомобиль успешно удалён.")  # добавляем сообщения которые можно использовать на фронте
            return super().delete(request, *args, **kwargs)  # вызываем метод базового класса для удаления
        else:
            messages.error(request,
                           "У вас нет прав на удаление этого автомобиля.")  # добавляем сообщения которые можно использовать на фронте
            return redirect('index')


class CarCreateView(LoginRequiredMixin, CreateView):
    form_class = CarAddForm
    template_name = 'cars/car_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form): #
        form.instance.owner = self.request.user # присваиваем создателя объекту машины
        return super().form_valid(form) # вызываем базовый метод класса

