from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from servidor.logic.servidor_logic import *


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def verificar(request):
    if request.method == 'POST':
        data = request.POST
        nombre = data.get('nombre')
        documento = data.get('documento')
        celular = data.get('celular')
        email = data.get('email')
        llavepublica = data.get('llave_publica')
        hash = data.get('hash')
        

        nombre_descifrado = decrypt_message(llavepublica,nombre)

        print(nombre_descifrado)
        

        response_data = {'status':'success',
                         'message':data}
        return JsonResponse(response_data,status=200)
        # Condicion si el hash es correcto
        # Condicion si no es correcto
    