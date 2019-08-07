from django.urls import path
from . import views

urlpatterns = [
    # for Create
    path('new/', views.new),
    path('create/', views.create),
    # for Read
    path('', views.index),
    # for Read detail
    path('<int:todo_id>/', views.detail),
]
