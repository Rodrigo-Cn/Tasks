from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from django.template import loader
from django.http import HttpResponse
from .forms import CursoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

def isAluno(user):
    return user.groups.filter(name='Alunos').exists()

def isProfessor(user):
    return user.groups.filter(name='Professores').exists()

@login_required
def cursos(request):
    getter = request.GET
    dic = {}

    if(getter):
        for key, value in getter.items():
            if key == "nome":
                dic[str(key)+"__contains"] = value

        if(isAluno(request.user)):
            template = loader.get_template("curso/home2.html")
        else:
            template = loader.get_template("curso/home.html")

        cursos = Curso.objects.filter(**dic)
        context = {'cursos': cursos, 'user': request.user}

    else:
        if(isAluno(request.user)):
            template = loader.get_template("curso/home2.html")
        else:
            template = loader.get_template("curso/home.html")

        cursos = Curso.objects.all()
        context = {'cursos': cursos, 'user': request.user}

    return HttpResponse(template.render(context, request))

@login_required
def detail(request,id):
    template = loader.get_template("curso/detail.html")
    curso = Curso.objects.get(pk=id)
    context = {'curso': curso}
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(isProfessor, login_url='/')
def add(request):

    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Curso adicionado com sucesso")
        return redirect('cursoshome')
    
    else:
        form = CursoForm()
        return render(request,"curso/add.html",{'form':form})

@login_required
@user_passes_test(isProfessor, login_url='/')
def edit(request, id):

    curso = Curso.objects.get(pk=id)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
        return redirect('cursoshome')
    
    else:
        form = CursoForm(instance=curso)
        return render(request,"curso/edit.html",{'form':form, 'curso':curso})

@login_required 
@user_passes_test(isProfessor, login_url='/')
def delete(request, id):
    curso = get_object_or_404(Curso, pk=id)
    curso.delete()
    return redirect('cursoshome')




