from django.shortcuts import render, redirect
from .forms import AddForm
from .models import Medico

# Create your views here.
def add_medico(request):
    django_form = AddForm(request.POST)
    # return redirect('app_medico/add_medico.html')
    if request.method == 'POST':
        
        if django_form.is_valid():
            django_form.save()

            return redirect('add_medico')
        else:
            django_form = AddForm()

    return render(request, 'app_medico/add_medico.html', {'form': django_form})