from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        
        labels = {
            'title': 'Titulo',
            'text': 'Texto',
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        labels = {
            'author': 'Autor',
            'text': 'Texto',
        }


class ContatoForm(forms.Form):
    emissor = forms.EmailField(required=True)
    assunto = forms.CharField(required=True)
    msg = forms.CharField(widget=forms.Textarea)