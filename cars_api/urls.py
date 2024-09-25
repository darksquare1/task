from django.urls import path
from cars_api.views import ListCarsApiView, RetrieveUpdateDestroyCarView, GetAddCommentsApiView

urlpatterns = [
    path('cars/', ListCarsApiView.as_view()),
    path('cars/<int:pk>/', RetrieveUpdateDestroyCarView.as_view()),
    path('cars/<int:pk>/comments/', GetAddCommentsApiView.as_view()),
]
