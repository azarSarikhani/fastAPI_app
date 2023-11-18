from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def welcome():
    """Returns a friendly welcome message!"""
    return {"message": "Hello World, welcome to this app!"}

@app.get("/hi")
async def root():
    return {"another page"}


@app.get("/items/{item_id}")
async def read_item(item_id : int):
    item_id = 3 + item_id
    return {"item_id": item_id}