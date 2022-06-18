from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,UpdateUserAPI

urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('update',UpdateUserAPI.as_view()),
]