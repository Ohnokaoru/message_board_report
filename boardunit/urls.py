from django.urls import path
from . import views

urlpatterns = [
    path("create-boardunit/", views.create_boardunit, name="create-boardunit"),
    path("review-all/", views.review_all, name="review-all"),
]
