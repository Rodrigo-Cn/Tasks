from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Disciplina
from django.template import loader
from django.http import HttpResponse
from .forms import DisciplinaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def isAluno(user):
    return user.groups.filter(name='Alunos').exists()

def isProfessor(user):
    return user.groups.filter(name='Professores').exists()

@login_required
def disciplinas(request):
    getter = request.GET
    dic = {}

    if(getter):
        for key, value in getter.items():
            if key == "nome":
                dic[str(key)+"__contains"] = value

        if(isAluno(request.user)):
            template = loader.get_template("disciplina/home2.html")
        else:
            template = loader.get_template("disciplina/home.html")

        disciplinas = Disciplina.objects.filter(**dic)
        context = {'disciplinas': disciplinas, 'user': request.user}

    else:
        if(isAluno(request.user)):
            template = loader.get_template("disciplina/home2.html")
        else:
            template = loader.get_template("disciplina/home.html")

        disciplinas = Disciplina.objects.all()
        context = {'disciplinas': disciplinas, 'user': request.user}

    return HttpResponse(template.render(context, request))

@login_required
def detail(request,id):
    template = loader.get_template("disciplina/detail.html")
    disciplina = Disciplina.objects.get(pk=id)
    context = {'disciplina': disciplina}
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(isProfessor, login_url='/')
def add(request):

    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('disciplinashome')
    
    else:
        form = DisciplinaForm
        return render(request,"disciplina/add.html",{'form':form})

@login_required
@user_passes_test(isProfessor, login_url='/')
def edit(request, id):

    disciplina = Disciplina.objects.get(pk=id)

    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
        return redirect('disciplinashome')
    
    else:
        form = DisciplinaForm(instance=disciplina)
        return render(request,"disciplina/edit.html",{'form':form, 'disciplina':disciplina})

@login_required 
@user_passes_test(isProfessor, login_url='/')
def delete(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    disciplina.delete()
    return redirect('disciplinashome')




