from fastapi import APIRouter
from services.external_api import (
    consultar_dolar_api,
    consultar_inflacion_argentina,
    consultar_open_library,
    consultar_poke_api,
    consultar_jikan_api,
)

router = APIRouter()

@router.get("/dolares")
def get_dolares():
    return {"status": "success", "data": consultar_dolar_api()}

@router.get("/inflacion")
def get_inflacion():
    return {"status": "success", "data": consultar_inflacion_argentina()}

@router.get("/libros")
def get_libros(q: str = "python"):
    return {"status": "success", "data": consultar_open_library(q)}

@router.get("/pokemon/{nombre}")
def get_pokemon(nombre: str):
    return {"status": "success", "data": consultar_poke_api(nombre)}

@router.get("/personaje-anime")
def get_personaje_anime(nombre: str):
    return {"status": "success", "data": consultar_jikan_api(nombre)}


