from django.shortcuts import render
import math
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
    return render(request, 'encuesta/ejercicio1.html',context)

def enviar1(request):
    resultado=0
    n1=int(request.POST['numero1'])
    n2=int(request.POST['numero2'])
    opr=request.POST['operacion']
    if opr=="suma":
        resultado=n1+n2
    elif opr=="resta":
        resultado=n1-n2
    elif opr=="multiplicacion":
        resultado=n1*n2
    context = {
        'numero1': n1,
        'numero2': n2,
        'resultado': resultado,
    }
    return render(request, 'encuesta/ejercicio1Respuesta.html', context)


def ejercicio2(request):

    context = {
        'titulo': "Cálculo del volumen de un cilindro",
    }
    return render(request, 'encuesta/ejercicio2.html',context)

def enviar2(request):
    resultado=0
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])

    resultado= math.pi*n1*((n2/2)**2)
    context = {
        'num1': n1,
        'num2': n2,
        'resultado': resultado,
    }
    return render(request, 'encuesta/ejercicio2Respuesta.html', context)