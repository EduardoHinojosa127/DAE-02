from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('enviar1', views.enviar1, name='enviar1'),
    path('ejercicio1/', views.ejercicio1, name='ejercicio1'),
]
