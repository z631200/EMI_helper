from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("api", views.PromptView.as_view()),
]