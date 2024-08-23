from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Turma
from django.template import loader
from django.http import HttpResponse
from .forms import TurmaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

def isAluno(user):
    return user.groups.filter(name='Alunos').exists()

def isProfessor(user):
    return user.groups.filter(name='Professores').exists()

@login_required
def turmas(request):
    getter = request.GET
    dic = {}

    if(getter):
        for key, value in getter.items():
            if key == "ano":
                dic[str(key)+"__contains"] = value

        if(isAluno(request.user)):
            template = loader.get_template("turma/home2.html")
        else:
            template = loader.get_template("turma/home.html")

        turmas = Turma.objects.filter(**dic)
        context = {'turmas': turmas, 'user': request.user}

    else:
        if(isAluno(request.user)):
            template = loader.get_template("turma/home2.html")
        else:
            template = loader.get_template("turma/home.html")

        turmas = Turma.objects.all()
        context = {'turmas': turmas, 'user': request.user}

    return HttpResponse(template.render(context, request))

@login_required
def detail(request,id):
    template = loader.get_template("turma/detail.html")
    turma = Turma.objects.get(pk=id)
    context = {'turma':turma}
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(isProfessor, login_url='/')
def add(request):

    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Turma adicionada com sucesso")
        return redirect('turmashome')
    
    else:
        form = TurmaForm()
        return render(request,"turma/add.html",{'form':form})

@login_required
@user_passes_test(isProfessor, login_url='/')
def edit(request, id):

    turma = Turma.objects.get(pk=id)

    if request.method == "POST":
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
        return redirect('turmashome')
    
    else:
        form = TurmaForm(instance=turma)
        return render(request,"turma/edit.html",{'form':form, 'turma':turma})

@login_required 
@user_passes_test(isProfessor, login_url='/')
def delete(request, id):
    turma = get_object_or_404(Turma, pk=id)
    turma.delete()
    return redirect('turmashome')

@login_required 
@user_passes_test(isProfessor, login_url='/')
def liststudents(request, id):
    template = loader.get_template("turma/list.html")
    turma = Turma.objects.get(pk=id)
    context = {'turma':turma}
    return HttpResponse(template.render(context, request))



