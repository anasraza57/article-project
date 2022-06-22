from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('article/<slug:slug>/', views.detail, name='detail'),
]