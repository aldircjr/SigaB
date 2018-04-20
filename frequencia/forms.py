from django import forms
from .models import Frequencia, Materia


class FrequenciaForm(forms.ModelForm):

    class Meta:
        model = Frequencia
        fields = ('presente',)

class MateriaForm(forms.ModelForm):

    alunos = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Frequencia.objects.all())

    class Meta:
        model = Materia
        fields = ('nome',)