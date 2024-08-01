from django.urls import path
from . import views

urlpatterns = [
    path('', views.disciplinas, name="disciplinashome"),
    path('detail/<int:id>/', views.detail, name="detail_disciplina"),
    path('add/', views.add,  name="add_disciplina"),
    path('edit/<int:id>/', views.edit, name="edit_disciplina"),
    path('delete/<int:id>/', views.delete, name="delete_disciplina"),
]