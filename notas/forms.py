from django import forms
from .models import Nota


class NotaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.fields["valorNota"].help_text = ""

    class Meta:
        model = Nota
        fields = ('valorNota', 'observacao',)

