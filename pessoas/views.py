from django.shortcuts import render, redirect
from alunos.forms import AlunosForm
from django.contrib.auth.models import Group

def add(request):
    if request.method == "POST":
        form = AlunosForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            group = Group.objects.get(id=1)
            user.groups.add(group)
            
            return redirect('taskshome')
    else:
        form = AlunosForm()
    
    return render(request, "registration/add.html", {'form': form})
