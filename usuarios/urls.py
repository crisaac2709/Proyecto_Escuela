from django.urls import path
from .views import registrar_alumno, registrar_profesor, HomeAlumno, HomeMaestro, loginView

app_name = "cuentas"

urlpatterns = [
    path('registrar_alumno/', registrar_alumno, name="registrar_alumno"),
    path('registrar_profesor/', registrar_profesor, name="registrar_profesor"),
    path('login/', loginView, name="login"),
    path('Home/Docente/', HomeMaestro, name="HomeMaestro"),
    path('Home/Alumno', HomeAlumno, name="HomeAlumno"),
]