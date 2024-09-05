from django.urls import path
from . import views

urlpatterns = [
    path("create-boardunit/", views.create_boardunit, name="create-boardunit"),
]
