from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404, JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Materia, Frequencia, Nota, Aluno
from .forms import FrequenciaForm, NotaForm, MateriaForm, AlunoForm




def mainPage(request):
    return render(request, 'frequencia/inicial.html')

@login_required
def listaMateria(request):
    materias = Materia.objects.order_by('nome')
    return render(request, 'notas/listaMateria.html', {'materias' : materias})
    
@login_required
def listaAluno(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    return render(request, 'notas/listaAluno.html', {'materia' : materia})
    
@login_required
def novoaluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.nome = form.cleaned_data['nome']
            aluno.cidade = form.cleaned_data['cidade']
            aluno.data_ingresso = timezone.now()
            aluno.save()
            return redirect('mainPage')
    else:
        form = AlunoForm()
    return render(request, 'frequencia/novoAluno.html', {'form' : form}) 

@login_required
def novamateria(request):
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            materia = form.save(commit=False)
            materia.nome = form.cleaned_data['nome']
            materia.professor_responsavel = form.cleaned_data['professor_responsavel']
            materia.save()
            form.save_m2m()
            return redirect('mainPage')
    else:

        form = MateriaForm()
    return render(request, 'frequencia/novaMateria.html', {'form' : form})

@login_required
def listaralunos(request):
    materias =  Materia.objects.order_by('nome')
    notas = Nota.objects.all()
    return render(request, 'frequencia/listaralunos.html',{'materias' : materias, 'notas':notas})

@login_required
def notas(request, pkMateria, pkAluno):
    materia = get_object_or_404(Materia, pk=pkMateria)
    aluno = get_object_or_404(Aluno, pk=pkAluno)
    
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.valorNota = form.cleaned_data['valorNota']
            nota.aluno = aluno
            nota.materia = materia
            nota.save()
            return render(request, 'frequencia/inicial.html')
    else:
        form = NotaForm()
    
    listaNotas = Nota.objects.filter(aluno=aluno, materia=materia)
    
    return render(request, 'notas/notas.html',{'aluno':aluno ,'materia':materia, 'form':form, 'listaNotas':listaNotas})

@login_required
def inserirNota(request, pkMateria, pkAluno, nota):
     try:
        materia = get_object_or_404(Materia, pk=pkMateria)
        aluno = get_object_or_404(Aluno, pk=pkAluno)

        notasDoAluno = Nota.objects.filter(materia=materia,aluno=aluno)

        notaAdd = Nota()
        notaAdd.aluno = aluno
        notaAdd.materia = materia
        notaAdd.valorNota = float(nota)
        notaAdd.save()

        post_json = {'status': 1}
     except Exception as e:
        post_json = {'status': 10}

     return JsonResponse(post_json)

@login_required
def atualizaNotaAjax(request, pkMateria, pkAluno):

    notasDoAluno = Nota.objects.filter(materia=pkMateria,aluno=pkAluno)    
    data = (dict(notas=list(notasDoAluno.values('valorNota',))))

    return JsonResponse(data)

@login_required
def materiaEdit(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == "POST":
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            materia = form.save(commit=False)
            materia.save()
            return redirect('listaralunos')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'frequencia/materiaEdit.html', {'form': form})

@login_required
def alunoEdit(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.save()
            return redirect('listaralunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'frequencia/alunoEdit.html', {'form': form})
