from django.urls import path
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

from cars_api.views import ListCarsApiView, RetrieveUpdateDestroyCarView, GetAddCommentsApiView

urlpatterns = [
    path('cars/', ListCarsApiView.as_view()),
    path('cars/<int:pk>/', RetrieveUpdateDestroyCarView.as_view()),
    path('cars/<int:pk>/comments/', GetAddCommentsApiView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name='schema'), name='redoc')
]
