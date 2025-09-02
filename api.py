from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Prueba Técnica API",
    description="API para probar habilidades básicas de Python",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la Prueba Técnica de Python API"}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

items: List[Item] = []

@app.get("/items", response_model=List[Item])
async def get_items(): 
    return items


# TODO: crear un endpoint POST /items para agregar un nuevo item a la lista


# TODO: Crear un endpoint GET /items/{item_index} para retornar un item por su índice


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)