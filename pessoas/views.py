from django.shortcuts import render, redirect
from professores.forms import ProfessoresForm
from django.contrib.auth.models import Group

def add(request):
    if request.method == "POST":
        form = ProfessoresForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            group = Group.objects.get(id=2)
            user.groups.add(group)
            
            return redirect('taskshome')
    else:
        form = ProfessoresForm()
    
    return render(request, "registration/add.html", {'form': form})
