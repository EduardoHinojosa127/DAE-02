from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('enviar1', views.enviar1, name='enviar1'),
    path('ejercicio1/', views.ejercicio1, name='ejercicio1'),
    path('enviar2', views.enviar2, name='enviar2'),
    path('ejercicio2/', views.ejercicio2, name='ejercicio2'),
]
