import requests
from modelos.todo import Todo as tarea

def consulta_api():
    direccion = "https://jsonplaceholder.typicode.com/todos"
    try: 
        respuesta = requests.get(direccion)
        respuesta.raise_for_status()
        
        tareas = [tareas()]
        if respuesta.status_code == 200:
            
            for todo in respuesta.json():
                
                nueva_tarea = tarea()
                nueva_tarea.userId = todo['userId']
                nueva_tarea.id = todo['id']
                nueva_tarea.title = todo['title']
                nueva_tarea.completed = todo['completed']
                tareas.append(nueva_tarea)
        print(tareas)
    
    except requests.exceptions.Timeout:
        print("Se sobrepaso el tiempo de espera")
    
    except requests.exceptions.ConnectionError:
        print("Hay un problema de comunicación con el servidor")

    except requests.exceptions.RequestException as error:
        print("Error en la solicitud: {error}")