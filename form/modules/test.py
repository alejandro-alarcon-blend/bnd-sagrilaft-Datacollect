import base64
import json
import requests
import time


def enviar_archivos(archivos, empresa, persona):
    # Crear una lista para los archivos procesados
    files_list = []
    webhook_url = "https://defaultb1aae949a5ef4815b7aff7c4aa546b.28.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/4bc6726a09aa4e94a12fd73e61d2d3e2/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=fFHbjCPOGUMvBDsPdTzRbZRXpCdde5wraCe9CdlVfJ4"
    
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
    
    datos_empresa = {
      "nombre": empresa.nombre,
      "nit": empresa.nit,
      "email": empresa.email,
      "telefono": empresa.tel
    }

    datos_persona = {
      "nombres": persona.nombres,
      "apellidos": persona.apellidos,
      "id": persona.id
    }
  
    # Crear el cuerpo de la solicitud con los archivos y metadata
    payload = {
        "files": files_list,
        "empresa": datos_empresa,
        "rep_legal": datos_persona
    }

    # Enviar la solicitud HTTP
    response = requests.post(webhook_url, json=payload)
    return response.status_code, response.text