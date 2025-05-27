from fastapi import FastAPI
from app.routes import user_routes, pedido_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(pedido_routes.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a PandaTaT API"}
