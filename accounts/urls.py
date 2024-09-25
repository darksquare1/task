from django.urls import path
from accounts.views import SignUpView, SignUpApiView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api/signup/', SignUpApiView.as_view())
]
