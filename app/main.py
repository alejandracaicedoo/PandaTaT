from fastapi import FastAPI
from app.routes import user_routes, pedido_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(pedido_routes.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a PandaTaT API"}
@app.post("/users/")
def create_user(user: dict):
    return {"message": "Usuario creado", "user": user}
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    return {"message": f"Usuario {user_id} actualizado", "user": user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"Usuario {user_id} eliminado"}