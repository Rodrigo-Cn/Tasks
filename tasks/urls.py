from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name="taskshome"),
    path('detail/<int:id>/', views.detail),
    path('add/', views.add),
    path('edit/<int:id>/', views.edit, name="edit_task"),
    path('delete/<int:id>/', views.delete, name="delete_task"),
]