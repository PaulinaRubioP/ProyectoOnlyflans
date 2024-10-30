from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes_publicos': flanes_publicos,
        'flanes_privados': flanes_privados,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes_privados': flanes_privados,
    }
    return render(request, 'welcome.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactFormModelForm()
    
    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def goodbye_view(request):
    return render(request, 'goodbye.html')

