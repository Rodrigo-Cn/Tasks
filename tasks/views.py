from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from django.template import loader
from django.http import HttpResponse
from .forms import TasksForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def isAluno(user):
    return user.groups.filter(name='Alunos').exists()

def isProfessor(user):
    return user.groups.filter(name='Professores').exists()

@login_required
def tasks(request):
    getter = request.GET
    dic = {}

    if(getter):
        for key, value in getter.items():
            if key == "titulo":
                dic[str(key)+"__contains"] = value

        if(isAluno(request.user)):
            template = loader.get_template("tasks/home2.html")
        else:
            template = loader.get_template("tasks/home.html")

        tarefas = Tasks.objects.filter(**dic)
        context = {'tarefas': tarefas, 'user': request.user}

    else:
        if(isAluno(request.user)):
            template = loader.get_template("tasks/home2.html")
        else:
            template = loader.get_template("tasks/home.html")

        tarefas = Tasks.objects.all()
        context = {'tarefas': tarefas, 'user': request.user}

    return HttpResponse(template.render(context, request))

@login_required
def detail(request,id):
    template = loader.get_template("tasks/detail.html")
    tarefa = Tasks.objects.get(pk=id)
    context = {'tarefa': tarefa}
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(isProfessor, login_url='/')
def add(request):

    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('taskshome')
    
    else:
        form = TasksForm
        return render(request,"tasks/add.html",{'form':form})

@login_required
@user_passes_test(isProfessor, login_url='/')
def edit(request, id):

    task = Tasks.objects.get(pk=id)

    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('taskshome')
    
    else:
        form = TasksForm(instance=task)
        return render(request,"tasks/edit.html",{'form':form, 'task':task})

@login_required 
@user_passes_test(isProfessor, login_url='/')
def delete(request, id):
    task = get_object_or_404(Tasks, pk=id)
    task.delete()
    return redirect('taskshome')

