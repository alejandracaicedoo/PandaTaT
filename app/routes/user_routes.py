from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def listar_usuarios():
    return {"mensaje": "Lista de usuarios (simulada)"}

@router.post("/")
def crear_usuario(usuario: dict):
    return {"mensaje": "Usuario creado", "usuario": usuario}

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    return {"usuario_id": usuario_id, "mensaje": "Información del usuario"}

@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: dict):
    return {"mensaje": f"Usuario {usuario_id} actualizado", "usuario": usuario}

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    return {"mensaje": f"Usuario {usuario_id} eliminado"}
