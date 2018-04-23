from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.decorators import login_required
from frequencia import models
from .forms import NotaForm



@login_required
def listaMateria(request):
    materias = models.Materia.objects.order_by('nome')
    return render(request, 'notas/listaMateria.html', {'materias' : materias})
    
@login_required
def listaAluno(request, pk):
    materia = get_object_or_404(models.Materia, pk=pk)
    return render(request, 'notas/listaAluno.html', {'materia' : materia})
    
@login_required
def notas(request, pkMateria, pkAluno):
    materia = get_object_or_404(models.Materia, pk=pkMateria)
    aluno = get_object_or_404(models.Aluno, pk=pkAluno)
    
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.valorNota = form.cleaned_data['valorNota']
            nota.observacao = form.cleaned_data['observacao']
            nota.aluno = aluno
            nota.materia = materia
            nota.save()
            return render(request, 'frequencia/inicial.html')
    else:
        form = NotaForm()
               
    
    return render(request, 'notas/notas.html',{'aluno':aluno ,'materia':materia, 'form':form})