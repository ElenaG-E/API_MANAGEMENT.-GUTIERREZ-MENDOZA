def buscar_usuario(busqueda):

    data = acceso_db.leer_datos(consulta)
    return data

def insertar_nuevo_usuario(usuario = usuario()):
    consulta = f"""
        INSERT INTO users(id_user, name, username, email, id_address, phone, website, id_company) VALUES
        ((usuario.id_user), (usuario.name), (usuario.username), (usuario.email), (usuario.id_address), (usuario.phone), (usuario.website))
    """
    id = acceso_db.insertar_datos(consulta)

def insertar_varios_usuarios(usuarios = [usuario()]):
    consulta = f"""
        INSERT INTO users(id_user, name, username, email, id_address, phone website, id_company) VALUES
        (%S, %S, %S, %S, %S, %S, %S)

