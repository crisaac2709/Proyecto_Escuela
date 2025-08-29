from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Maestro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='profesores/', blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.user.username}'
    
    
    
class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="estudiantes/", blank=True, null=True)
    codigo = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f'{self.user.username}'
