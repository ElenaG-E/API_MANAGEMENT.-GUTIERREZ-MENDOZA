import negocios.procesar_urls as neg_url
import requests
import json

def obtener_usuarios_api():
    direccion = neg_url.url_servicio("users")
    
    try:
        respuesta = requests.get(direccion)
        print(respuesta)
        respuesta.raise_for_status()

        if respuesta.status_code == 200:
            return respuesta.json()

    except requests.exceptions.Timeout:
        print("Se sobrepasó el timepo de espera para la respuesta.")

    except requests.exceptions.ConnectionError:
        print("Hay un problema de comunicación con le servidor.")
    
    except requests.exceptions.RequestException as error: 
        print(f"Error en la solicitud: {error}")

def obtener_usuario_id_api(usuario):
    direccion = neg_url("users")
    direccion_servicio = f"{direccion}/{usuario.id_user}"

    try:
        respuesta = requests.get(direccion_servicio)
        print(respuesta)
        respuesta.raise_for_status()

        if respuesta.status_code == 200:
            return respuesta.json()

    except requests.exceptions.Timeout:
        print("Se sobrepasó el timepo de espera para la respuesta.")

    except requests.exceptions.ConnectionError:
        print("Hay un problema de comunicación con le servidor.")
    
    except requests.exceptions.RequestException as error: 
        print(f"Error en la solicitud: {error}")
