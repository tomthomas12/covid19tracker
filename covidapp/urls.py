from django.contrib import admin
from django.urls import path
from .views import helloword
urlpatterns = [
    path('hello/',helloword),
]
