from django.shortcuts import render, redirect
from .forms import PessoasForm
from django.contrib.auth.models import Group

def add(request):
    if request.method == "POST":
        form = PessoasForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            group = Group.objects.get(id=1)
            user.groups.add(group)
            
            return redirect('taskshome')
    else:
        form = PessoasForm()
    
    return render(request, "registration/add.html", {'form': form})
