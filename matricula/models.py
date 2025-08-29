from django.db import models
from usuarios.models import Alumno, Maestro
from cursos.models import Materia

# Create your models here.
class Matricula(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='matriculas')
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='matriculas')

    class Meta:
        unique_together = ('alumno', 'materia')
    
    def __str__(self):
        return f'{self.alumno} - {self.materia}'
    



class Evaluacion(models.Model):
    titulo = models.CharField(max_length=50)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('materia', 'titulo')

    def __str__(self):
        return f'{self.titulo} - {self.materia}'
    


class Nota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    class Meta:
        unique_together = ('matricula', 'evaluacion')

    def __str__(self):
        return f'{self.evaluacion} - {self.valor}'