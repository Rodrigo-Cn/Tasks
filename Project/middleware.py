from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from professores.models import Professor
from django.core.exceptions import PermissionDenied
from django.urls import resolve

class PagamentoMensal(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = resolve(request.path_info).url_name
        
        if current_url == 'login':
            return self.get_response(request)

        if request.user.is_authenticated:
            user = request.user

            if user.groups.filter(id=2).exists():
                try:
                    professor = Professor.objects.get(pk=user.pk)

                    if not professor.is_valid():
                        raise PermissionDenied("A validade do professor expirou.")
                    
                except Professor.DoesNotExist:
                    raise PermissionDenied("Usuário não encontrado como professor.")
        
        else:
            return redirect('login')

        return self.get_response(request)
