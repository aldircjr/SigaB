from django import forms
from .models import Frequencia, Materia, Nota, Aluno
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
        
        #widgets ={
        #    'presente': forms.CheckboxSelectMultiple(
        #        attrs={'class': 'presente',
        #        }),
        #    }
        
        
        
class NotaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.fields["valorNota"].help_text = ""

    class Meta:
        model = Nota
        fields = ('valorNota', 'observacao',)


class MateriaForm(forms.ModelForm):

    class Meta:
        model = Materia
        fields = ('nome', 'professor_responsavel', 'alunos')



class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('nome', 'cidade')