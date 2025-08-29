from django.db import models
from usuarios.models import Alumno, Maestro


# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    creditos = models.PositiveSmallIntegerField(default=1)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre}'


