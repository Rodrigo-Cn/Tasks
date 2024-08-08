from django.urls import path, register_converter
from . import views
import uuid


urlpatterns = [
    path('', views.cursos, name="cursoshome"),
    path('detail/<uuid:id>/', views.detail, name="detail_curso"),
    path('add/', views.add,  name="add_curso"),
    path('edit/<uuid:id>/', views.edit, name="edit_curso"),
    path('delete/<uuid:id>/', views.delete, name="delete_curso"),
]