from django.urls import path
from .views import UserView, UserDetailsView
from rest_framework_simplejwt import views
from .views import LoginJWTView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailsView.as_view()),
    path("users/login/", LoginJWTView.as_view()),
    path("login/refresh/", views.TokenRefreshView.as_view())]
