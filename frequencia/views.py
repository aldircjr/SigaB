from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from .models import Materia, Frequencia
from .forms import FrequenciaForm



def mainPage(request):
    return render(request, 'frequencia/inicial.html')

@login_required
def frequencia(request):
	materias = Materia.objects.order_by('nome')
	return render(request, 'frequencia/listaMateria.html', {'materias' : materias})
	
@login_required
def frequenciaDetails(request, pk):
	materia = get_object_or_404(Materia, pk=pk)
	frequencia = Frequencia()
	frequencia.materia = materia
	return render(request, 'frequencia/frequencia.html', {'materia' : materia, 'frequencia' : frequencia})
	
@login_required
def frequenciaNew(request,pk):

    materia = get_object_or_404(Materia, pk=pk)
    if request.method == "POST":
        form = FrequenciaForm(request.POST)
        if form.is_valid():
            #post.save()
            return redirect('mainPage')
    else:
        form = FrequenciaForm()
    return render(request, 'frequencia/frequencia.html', {'materia' : materia, 'form' : form})