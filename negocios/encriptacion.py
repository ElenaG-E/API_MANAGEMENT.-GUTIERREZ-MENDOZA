from cryptography.fernet import Fernet
from auxiliares.clave_fernet import ClaveGenerada

def encriptar(contrasena):
    clave_encriptacion = Fernet(ClaveGenerada)
    contrasena_encriptada = clave_encriptacion.encrypt(contrasena.encode('utf-8'))
    return contrasena_encriptada


def desencriptar(contrasena_encriptada):
    clave_encriptacion = Fernet(ClaveGenerada)
    contrasena_desencriptada = clave_encriptacion.decrypt(contrasena_encriptada)
    return contrasena_desencriptada