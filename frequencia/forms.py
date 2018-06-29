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
        
        
class NotaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.fields["valorNota"].help_text = ""

    class Meta:
        model = Nota
        fields = ('valorNota',)


class MateriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['professor_responsavel'].widget.attrs['class'] = 'form-control'
        self.fields['alunos'].widget.attrs['class'] = 'form-control'    

    class Meta:
        model = Materia
        fields = ('nome', 'professor_responsavel', 'alunos')



class AlunoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AlunoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Aluno
        fields = ('nome', 'cidade')