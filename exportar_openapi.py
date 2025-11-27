# Exporta el contrato OpenAPI de tu servicio FastAPI
# Ejecuta este script en la misma carpeta donde corre tu FastAPI

import requests
import json

# Cambia la URL si tu servicio no está en localhost:8000
url = "http://127.0.0.1:8000/openapi.json"

r = requests.get(url)
if r.status_code == 200:
    with open("openapi_clima.json", "w", encoding="utf-8") as f:
        json.dump(r.json(), f, ensure_ascii=False, indent=2)
    print("Contrato OpenAPI exportado como openapi_clima.json")
else:
    print(f"Error al obtener OpenAPI: {r.status_code}")
