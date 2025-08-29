from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Alumno, Maestro
import os

User = get_user_model()

class BaseUserCrearForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        

class ProfesorRegistroForm(BaseUserCrearForm):
    titulo = forms.CharField(max_length=100)
    imagen = forms.ImageField()
    
    def clean_codigo(self):
        codigo = self.cleaned_data['titulo'].strip()
        if codigo < 5:
            raise forms.ValidationError('Minimo son 5 caracteres')
        return codigo
        
    def clean_imagen(self):
        archivo = self.cleaned_data.get('imagen')
        
        if not archivo:
            return archivo
        
        nombre = (archivo.name or "").lower()
        if not (nombre.endswith('.png') or nombre.endswith('.jpg') or nombre.endswith('.jpeg')):
            raise forms.ValidationError('Solo se permiten imagenes en extensiones ".png", ".jpg", ".jpeg"')
        # Osea 2 mb
        max_bytes = 2 * 1024 * 1024
        if archivo.size > max_bytes:
            raise forms.ValidationError('La imagen no puede pesar más de 2 MB.')
        
        return archivo
    
    
class AlumnoRegistroForm(BaseUserCrearForm):
    codigo = forms.CharField(max_length=20)
    imagen = forms.ImageField()
    
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo').strip()
        if len(codigo) < 5:
            raise forms.ValidationError('Minimo son 5 caracteres')
        
        codigo = Alumno.objects.filter(codigo = codigo)
        if codigo:
            raise forms.ValidationError('Este codigo ya existe')
        
        return codigo
        
    def clean_imagen(self):
        archivo = self.cleaned_data.get('imagen')
        
        if not archivo:
            return archivo
        
        nombre = (archivo.name or "").lower()
        if not (nombre.endswith('.png') or nombre.endswith('.jpg') or nombre.endswith('.jpeg')):
            raise forms.ValidationError('Solo se permiten imagenes en extensiones ".png", ".jpg", ".jpeg"')
        
        # Osea 2 mb
        max_bytes = 2 * 1024 * 1024
        if archivo.size > max_bytes:
            raise forms.ValidationError('La imagen no puede pesar más de 2 MB.')
        
        return archivo