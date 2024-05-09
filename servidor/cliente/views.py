# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cliente.logic.cliente_logic import *


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
        hash_data = data.get('hash')
        

        nombre_descifrado = decrypt_message(llavepublica,nombre)
        documento_descifrado = decrypt_message(llavepublica,documento)
        celular_descifrado = decrypt_message(llavepublica,celular)
        email_descifrado = decrypt_message(llavepublica,email)

        data_concatenada =  nombre_descifrado + documento_descifrado +celular_descifrado + email_descifrado
        data_concatenada_hash = calculate_hash(data_concatenada)

        if(data_concatenada_hash == hash_data):
            # guardamos el objeto de cliente
            # devolvemos respuesta de que si funciono la cosa
            print("Los Hash si son iguales")
        else:
            # devolvemos respuesta de que las cosas no funcionaron
            print("Los hash son diferentes")

        response_data = {'status':'success',
                         'message':data}
        return JsonResponse(response_data,status=200)