from django.contrib import admin
from django.urls import path, include
from tasks import urls
from accounts import urls
from disciplinas import urls
from cursos import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('disciplina/',include('disciplinas.urls')),
    path('curso/',include('cursos.urls')),
    path("accounts/",include('pessoas.urls')),
    path("accounts/",include('django.contrib.auth.urls')),
]
