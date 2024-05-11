import requests
import json
from scapy.all import sniff
from scapy.layers.http import HTTPRequest

def interceptar_peticion(url, data):
    # Decifrar los datos cifrados
    data_cifrada = {
        'nombre': 'nuevo_nombre',  # Modifica el valor aquí
        'documento': data.get('documento'),
        'celular': data.get('celular'),
        'email': data.get('email'),
        'llave_publica': data.get('llave_publica'),
        'hash': data.get('hash'),
        'form': data.get('form')
    }
    
    try:
        response = requests.post(url, json=data_cifrada)
        response.raise_for_status()  # Levanta una excepción en caso de error HTTP
        return response
    except requests.exceptions.RequestException as e:
        print("Error al enviar la solicitud:", e)
        return None

def capture_next_request():
    # Capturar la siguiente petición HTTP usando Scapy
    paquetes = sniff(filter="tcp and dst host localhost and dst port 8001", lfilter=lambda x: x.haslayer(HTTPRequest), store=False)
    print(paquetes)
    
    # Extraer los datos de la petición
    peticion = paquetes[0]
    data_peticion = peticion[HTTPRequest].payload
    
    # Convertir los datos a JSON
    datos_json = json.loads(data_peticion.decode('utf-8'))
    
    # Devolver los datos de la petición
    return datos_json

def main():
    while True:
        print("holi")
        # Capturar la siguiente petición HTTP
        request = capture_next_request()
        print("holi")

        # Verificar si la petición es para la URL especificada
        if request :
            response = interceptar_peticion("http://localhost:8001/verificar/", request)

            if response is not None:
                print("Respuesta recibida:", response.status_code)

if __name__ == "__main__":
    main()
