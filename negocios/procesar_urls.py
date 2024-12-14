import auxiliares.urls as url

def url_servicio(origen):
    direccion = f"{url.url_base_jsonplaceholder}/{origen}"
    return direccion