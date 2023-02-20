from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse('Hola Django - Coder')

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):
        dia = datetime.datetime.now()
        documentoDeTexto = f"Hoy es día: <br> {dia}"
        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f'Mi nombre es: <br><br> {nombre}'
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    nom = 'Daniel'
    ap = 'Gonzalez'
    listaDeNotas = [2, 2, 3, 7, 2, 5]
    diccionario = {'nombre':nom, 'apellido':ap, 'hoy':datetime.datetime.now(), 'notas':listaDeNotas}
    miHtml = open('C:/Users/Danie/OneDrive/Escritorio/PythonProject1/Proyecto1/Proyecto1/planillas/template1.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)