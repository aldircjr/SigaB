from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    data_ingresso = models.DateField()


    def salvar(self):
        self.save()

    def getMaterias(self):
        return self.materias

    def __str__(self):
        return self.nome

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    professor_responsavel = models.CharField(max_length=20)
    alunos = models.ManyToManyField(Aluno, blank=True)

    def contaAlunos(self):
        return self.alunos.count

    def __str__(self):
        return self.nome

    def __index__(self):
        return self.alunos.count
    
    def getId(self):
        return self.id

class Frequencia(models.Model):

    id = models.AutoField(primary_key=True)
    materia = models.ForeignKey(Materia, related_name='frequencia')
    data = models.DateField()
    presente = models.ManyToManyField(Aluno)
    

    def salvar(self):
        #self.data = timezone.now()
        self.save()
        
    def __str__(self):
        return self.data.strftime('%d/%m/%Y')
