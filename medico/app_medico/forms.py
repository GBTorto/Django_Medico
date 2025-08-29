from django import forms
from .models import Medico

class AddForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = ('__all__')