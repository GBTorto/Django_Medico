from django import forms
from .models import Medico

class AddForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = ('__all__')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.TextInput(attrs={'class': 'form-control'}),
            'crm': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
        }