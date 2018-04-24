from django import forms
from .models import Frequencia, Materia
from django.forms import ModelForm


class FrequenciaForm(forms.ModelForm):

    #presente = forms.ModelMultipleChoiceField(queryset=materia.alunos)

    def __init__(self, *args, **kwargs):
        materia = kwargs.pop('materia')
        super(FrequenciaForm, self).__init__(*args, **kwargs)
        self.fields["presente"].queryset = materia.alunos
        self.fields["data"].help_text = "dd/mm/aaaa"



    class Meta:
        model = Frequencia
        fields = ('presente','data',)
        

        
        
