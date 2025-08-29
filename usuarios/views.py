from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno, Maestro
from django.contrib.auth import get_user_model
from .forms import AlumnoRegistroForm, ProfesorRegistroForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

User = get_user_model()


# Create your views here.
def registrar_profesor(request):
    if request.method == 'POST':
        form = ProfesorRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            titulo = form.cleaned_data.get('titulo')
            imagen = form.cleaned_data.get('imagen')
            Maestro.objects.create(
                user = user,
                titulo = titulo,
                imagen = imagen
            )
            messages.success(request, 'Maestro creado correctamente')
            return redirect('usuarios:login')
        messages.error(request, 'Revisa los errores del formulario')
    else:
        form = ProfesorRegistroForm()
    
    return render(request, 'RegisterMaestro.html', {'form': form})


def registrar_alumno(request):
    if request.method == 'POST':
        form = AlumnoRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            codigo = form.cleaned_data.get('codigo')
            imagen = form.cleaned_data.get('imagen')
            Alumno.objects.create(
                user = user, 
                codigo = codigo,
                imagen = imagen
            )
            messages.success(request, 'Alumno creado correctamente')
            return redirect('usuarios:login')
        messages.error(request, 'Revisa los errores del formulario')
    else:
        form = AlumnoRegistroForm()
        
    return render(request, 'RegisterAlumno.html', {'form':form})



def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        usuario = authenticate(request, username = username, password = password)
        
        if usuario:
            login(request, usuario)
            messages.success(request, f'{usuario.username} iniciaste  sesion correctamente ')
            if hasattr(usuario, 'maestro'):
                return redirect('usuarios:HomeMaestro')
            elif hasattr(usuario, 'alumno'):
                return redirect('usuarios:HomeAlumno')
        else:
            messages.error(request, 'Credenciales invalidas')
    
    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    messages.info(request, 'Sesion cerrada')
    return redirect('')

from .access import solo_alumnos, solo_profesores

@login_required
@solo_alumnos
def HomeAlumno(request):
    return render(request, 'HomeAlumno.html')

@login_required
@solo_profesores
def HomeMaestro(request):
    profesor = get_object_or_404(Maestro, user = request.user)
    return render(request, 'HomeMaestro.html', {'profesor':profesor})