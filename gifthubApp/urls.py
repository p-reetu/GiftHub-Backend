from django.urls import path
from .views import GiftsView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('gifts',GiftsView.as_view())
]