from django.contrib import admin
from .models import Aluno, Materia, Frequencia, Nota
# Register your models here.

admin.site.register(Aluno)
admin.site.register(Materia)
admin.site.register(Frequencia)
admin.site.register(Nota)
