import requests
import base64

TOKEN = "TU_TOKEN" 
API_URL = "TU_URL_A_LA_BASE_DE_DATOS"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

datos = requests.get(API_URL, headers=HEADERS).json()
contenido_original = base64.b64decode(datos['content']).decode('utf-8')

contenido_limpio = contenido_original.rstrip()

nueva_fila = "\n2,Mujer,1,De 15 a 30 minutos,2,Auto particular,1,0.25"

contenido_final = contenido_limpio + nueva_fila

payload = {
    "message": "Añadir fila sin espacios vacios",
    "content": base64.b64encode(contenido_final.encode()).decode(),
    "sha": datos['sha']
}

requests.put(API_URL, json=payload, headers=HEADERS)
print("Hecho.")