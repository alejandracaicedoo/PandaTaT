from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def listar_usuarios():
    return {"mensaje": "Lista de usuarios (simulada)"}
