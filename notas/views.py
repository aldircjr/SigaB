from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def notas(request):
    #materias = Materia.objects.order_by('nome')
    return render(request, 'notas/notas.html')