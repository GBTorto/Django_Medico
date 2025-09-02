from django import forms
from .models import Especialidade

class AddForm(forms.ModelForm):

    class Meta:
        model = Especialidade
        fields = '__all__'

# de Gabriel Morais