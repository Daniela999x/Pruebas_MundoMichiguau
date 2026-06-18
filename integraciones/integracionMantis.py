import requests
import base64
import os

TOKEN = "TOKEN_PERSONAL"
BASE_URL = "https://mantistcy.cl/mantis/api/rest/issues"

PROYECTO = "grupo1 - Reyes - Toledo - Zuñiga - Mella - Rodriguez - Contreras"
CATEGORIA = "Caja Negra"


def enviar_resultado_mantis(
    resumen,
    descripcion,
    resultado_esperado,
    resultado_obtenido,
    tipo_prueba="Funcional ",
    evidencia=None
):
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "summary": resumen,
        "description": descripcion,
        "project": {"name": PROYECTO},
        "category": {"name": CATEGORIA},
        "custom_fields": [
            {
                "field": {"name": "Resultado Esperado"},
                "value": resultado_esperado
            },
            {
                "field": {"name": "Resultado Obtenido"},
                "value": resultado_obtenido
            },
            {
                "field": {"name": "Tipo Prueba"},
                "value": tipo_prueba
            }
        ]
    }

    response = requests.post(BASE_URL, json=payload, headers=headers)

    print("Código:", response.status_code)
    print("Respuesta:", response.text)

    if response.status_code == 201 and evidencia is not None:
        issue_id = response.json()["issue"]["id"]
        adjuntar_evidencia(issue_id, evidencia)

    return response.status_code, response.text


def adjuntar_evidencia(issue_id, ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("No se encontró la evidencia:", ruta_archivo)
        return

    with open(ruta_archivo, "rb") as archivo:
        contenido_base64 = base64.b64encode(archivo.read()).decode("utf-8")

    nombre_archivo = os.path.basename(ruta_archivo)

    payload = {
        "files": [
            {
                "name": nombre_archivo,
                "content": contenido_base64
            }
        ]
    }

    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }

    url = f"{BASE_URL}/{issue_id}/files"

    response = requests.post(url, json=payload, headers=headers)

    print("Código adjunto:", response.status_code)
    print("Respuesta adjunto:", response.text)