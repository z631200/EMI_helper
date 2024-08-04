from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("api", views.FileView.as_view(), name="file_view"),
]
