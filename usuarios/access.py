from django.http import HttpResponseForbidden
from functools import wraps

def solo_profesores(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'maestro'):
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acceso solo para profesores")
    return wrapper

def solo_alumnos(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'alumno'):
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acceso solo para alumnos")
    return wrapper
