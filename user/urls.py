from django.urls import path
from . import views

urlpatterns = [
    path("user-register/", views.user_register, name="user-register"),
    path("chalogin/", views.chalogin, name="chalogin"),
    path("user-logout/", views.user_logout, name="user-logout"),
]
