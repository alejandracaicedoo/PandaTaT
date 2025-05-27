from fastapi import APIRouter
from app.models.database import get_connection

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.get("/enviados")
def pedidos_enviados():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pedidos WHERE estado_id = 1")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"pedidos_enviados": data}
