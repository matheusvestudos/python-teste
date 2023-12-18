# Primeiro, importe as bibliotecas padrão
from typing import Union

# Depois, importe as bibliotecas de terceiros
import uvicorn
from fastapi import FastAPI

# Código da aplicação
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
