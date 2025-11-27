from fastapi import FastAPI, Query
import requests


app = FastAPI(
    title="Servicio de Clima Actual",
    description="API REST para consultar el clima actual por país y ciudad. Ideal para integración MCP.",
    version="1.0.0",
    contact={
        "name": "Soporte Clima",
        "email": "soporte@ejemplo.com"
    }
)

# Diccionario de coordenadas de ejemplo (puedes ampliarlo)
COORDS = {
    ("peru", "lima"): {"lat": -12.04, "lon": -77.03},
    ("mexico", "cdmx"): {"lat": 19.43, "lon": -99.13},
    ("españa", "madrid"): {"lat": 40.4168, "lon": -3.7038},
    ("francia", "paris"): {"lat": 48.8566, "lon": 2.3522},
    ("eeuu", "nueva york"): {"lat": 40.7128, "lon": -74.0060},
    ("eeuu", "los angeles"): {"lat": 34.0522, "lon": -118.2437},
    ("brasil", "rio de janeiro"): {"lat": -22.9068, "lon": -43.1729},
    ("argentina", "buenos aires"): {"lat": -34.6037, "lon": -58.3816},
    ("chile", "santiago"): {"lat": -33.4489, "lon": -70.6693},
    ("colombia", "bogotá"): {"lat": 4.7110, "lon": -74.0721},
    ("japon", "tokio"): {"lat": 35.6895, "lon": 139.6917},
    ("italia", "roma"): {"lat": 41.9028, "lon": 12.4964},
    ("reino unido", "londres"): {"lat": 51.5074, "lon": -0.1278},
    ("alemania", "berlin"): {"lat": 52.5200, "lon": 13.4050},
    ("china", "pekin"): {"lat": 39.9042, "lon": 116.4074},
    ("australia", "sydney"): {"lat": -33.8688, "lon": 151.2093},
    ("canada", "toronto"): {"lat": 43.6532, "lon": -79.3832},
    ("india", "nueva delhi"): {"lat": 28.6139, "lon": 77.2090},
    ("turquia", "estambul"): {"lat": 41.0082, "lon": 28.9784},
    ("egipto", "el cairo"): {"lat": 30.0444, "lon": 31.2357},
    ("sudafrica", "ciudad del cabo"): {"lat": -33.9249, "lon": 18.4241}
}

from fastapi.responses import JSONResponse
from fastapi import status

@app.get(
    "/clima",
    summary="Obtener clima actual por país y ciudad",
    description="Devuelve el clima actual para una ciudad y país soportados.",
    response_description="Datos meteorológicos actuales de la ciudad."
)
def clima(
    pais: str = Query(..., description="Nombre del país en minúsculas, por ejemplo: 'peru'"),
    ciudad: str = Query(..., description="Nombre de la ciudad en minúsculas, por ejemplo: 'lima'")
):
    key = (pais.lower(), ciudad.lower())
    if key not in COORDS:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Ciudad no soportada. Usa /docs para ver las ciudades disponibles."}
        )
    coords = COORDS[key]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
    r = requests.get(url)
    data = r.json()["current_weather"]
    return {
        "pais": pais,
        "ciudad": ciudad,
        "temperatura": data["temperature"],
        "viento": data["windspeed"],
        "direccion_viento": data["winddirection"],
        "codigo_meteo": data["weathercode"]
    }