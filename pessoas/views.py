from django.shortcuts import render, redirect
from .forms import PessoasForm

def add(request):
    if request.method == "POST":
        form = PessoasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskshome')
    else:
        form = PessoasForm()
    
    return render(request, "registration/add.html", {'form': form})
