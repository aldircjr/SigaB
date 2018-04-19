from django.db import models
from frequencia import models as modelo

class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(modelo.Aluno)
    materia = models.ForeignKey(modelo.Materia)
    valorNota = models.FloatField(range(0,10))
	
	
	
   