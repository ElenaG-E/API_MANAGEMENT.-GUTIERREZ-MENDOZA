import mysql.connector
from mysql.connector import errorcode

def generar_conexion():
    config={
        # 'host': host,
        # 'user': user,
        # 'password': password,
        # 'database': database
        'host': "localhost",
        'user': "evaluacion",
        'password': "a1b2c3d4e5",
        'database': "evaluacion_3"
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion and conexion.is_connected():
            return conexion
        else:
            print("No fue posible conectarse a la base de datos.")
    
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado, usuario o contraseña incorrectos.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe")
        else:
            print(error)
    else:
        conexion.close()