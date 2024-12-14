import os
from cryptography.fernet import Fernet

def generacion_clave():
    clave = Fernet.generate_key()
    guardar_clave = f"ClaveGenerada = {clave}"

    file = "clave_fernet.py"
    ubicacion = os.path.join('auxiliares', file)
    ubicacion = os.path.abspath(ubicacion)
    ubicacion = os.path.realpath(ubicacion)
    archivo = open(f"{ubicacion}", "+w")
    archivo.write(guardar_clave)
    archivo.close()
