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
    # for update
    path('<int:todo_id>/edit/', views.edit),
    path('<int:todo_id>/update/', views.update),
    # for delete
    path('<int:todo_id>/delete/', views.delete),
]
