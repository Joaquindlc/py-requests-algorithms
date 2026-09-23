import requests
from core.config import settings

# OpenLibrary (Busqueda de libros por tema o titulo)
def consultar_open_library(busqueda: str = "python") -> dict:
    params = {"q": busqueda}
    try:
        response = requests.get(settings.OPEN_LIBRARY_API_URL, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error al consultar Open Library: {error}")
        return {}

# DolarAPI (Cotizaciones de dolares en Argentina)
def consultar_dolar_api() -> list:
    
    try:
        response = requests.get(settings.DOLAR_API_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error al consultar DolarAPI: {error}")
        return []

# ArgentinaDatos (Indices Economicos)
def consultar_inflacion_argentina() -> list:

    try:
        response = requests.get(settings.ARGENTINA_DATOS_API_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error al consultar ArgentinaDatos: {error}")
        return []

# PokeAPI
def consultar_poke_api(nombre: str) -> dict:
    url = f"{settings.POKE_API_URL}/{nombre.lower()}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error al consultar POKEAPI: {error}")
        return {}

# API de anime
def consultar_jikan_api(nombre: str) -> dict:
    params = {
        "q": nombre,
        "limit": 1
    }

    # agrego encabezado header para evitar el bloqueo de jikan
    headers = {
        "User-Agent": "ProyectoRequestsApp/1.0"
    }
    try:
        response = requests.get(
            settings.JIKAN_API_URL,
            params=params,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        json_data = response.json()

        # Jikan va a devolver el resultado dentro de la lista "data"
        lista_resultados = json_data.get("data", [])

        # Si encontramos el personaje, devolvemos el primero. sino un dict vacio
        if lista_resultados:
            return lista_resultados[0]
        return {}

    except requests.exceptions.RequestException as error:
        print(f"Error al consultar Jikan API: {error}")
        return {}
