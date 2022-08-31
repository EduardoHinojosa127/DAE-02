from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)


def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def ejercicio1(request):
    context = {
        'titulo': "Ejercicio1",
    }
    return render(request, 'encuesta/ejercicio1.html', context)

def enviar1(request):
    context = {
        'numero1': request.POST['numero1'],
        'numero2': request.POST['numero2'],
        'resultado': 'numero1'+'numero2',
    }
    return render(request, 'encuesta/ejercicio1Respuesta.html', context)