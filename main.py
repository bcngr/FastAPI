# Quick and simple API using python uvicorn and fastapi
#
# run:
#   uvicorn main:app --reload
#
# example endpoints: 
#
#   http://127.0.0.1:8000/items/123?q=example
#   http://127.0.0.1:8000/docs - Swagger
#   http://127.0.0.1:8000/redoc - Redoc


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello 123"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

