from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse( "Hola Pa") --- Respuesta al vuelo sin usar html directam al navegador

def index(request):
    context = {}
    context ['nombre_sitio'] = 'libros online'

    return render(request, 'index.html', context)
