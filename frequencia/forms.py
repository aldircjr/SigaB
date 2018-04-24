from django import forms
from .models import Frequencia, Materia
from django.forms import ModelForm


class FrequenciaForm(forms.ModelForm):

    #presente = forms.ModelMultipleChoiceField(queryset=materia.alunos)


    class Meta:
        model = Frequencia
        fields = ('presente','data',)
        
        
