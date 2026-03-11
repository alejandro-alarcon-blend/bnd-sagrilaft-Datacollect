import base64
import json
import requests

def generar_json_dinamico(archivos, metadata, webhook_url):
    # Crear una lista para los archivos procesados
    files_list = []
    
    # Iteramos sobre los archivos y los convertimos a base64
    for archivo in archivos:
        with open(archivo.path(), "rb") as f:
            contenido = f.read()

        archivo_base64 = base64.b64encode(contenido).decode('utf-8')

        # Agregamos cada archivo a la lista
        files_list.append({
            "filename": archivo.filename,
            "content": archivo_base64
        })
    
    # Crear el cuerpo de la solicitud con los archivos y metadata
    payload = {
        "files": files_list,
        "metadata": metadata
    }

    # Enviar la solicitud HTTP
    response = requests.post(webhook_url, json=payload)
    return response.status_code, response.text