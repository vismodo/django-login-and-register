from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register),
    path('signup/', views.signup),
]