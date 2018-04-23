from django.db import models
from frequencia import models as modelo
from django.core.validators import MaxValueValidator, MinValueValidator

class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(modelo.Aluno)
    materia = models.ForeignKey(modelo.Materia)
    valorNota = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    observacao = models.TextField(max_length=100, default='')
	
    
    def __str__(self):
        return self.aluno.nome + ' - ' + self.materia.nome + ' - Nota: ' + str(self.valorNota)
        
	
   