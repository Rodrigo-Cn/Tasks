from django.urls import path, register_converter
from . import views
import uuid


urlpatterns = [
    path('', views.turmas, name="turmashome"),
    path('detail/<int:id>/', views.detail, name="detail_turma"),
    path('add/', views.add,  name="add_turma"),
    path('edit/<int:id>/', views.edit, name="edit_turma"),
    path('delete/<int:id>/', views.delete, name="delete_turma"),
    path('alunos/<int:id>/', views.liststudents, name="listar_alunos"),
]