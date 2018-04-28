from django import forms
from .models import Frequencia, Materia, Nota
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
        

        
        
        
class NotaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.fields["valorNota"].help_text = ""

    class Meta:
        model = Nota
        fields = ('valorNota', 'observacao',)


