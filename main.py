from fastapi import FastAPI, HTTPException

import datetime
import uvicorn
from typing import List
from typing import Dict


dataBase = [
    {"id" : 1, "size" : "s", "color" : "green", "group" : "kids"},
    {"id" : 2, "size" : "s", "color" : "blue", "group" : "kids"},
    {"id" : 3, "size" : "s", "color" : "red", "group" : "kids"},
    {"id" : 4, "size" : "s", "color" : "gray", "group" : "kids"},
    {"id" : 5, "size" : "s", "color" : "pink", "group" : "kids"},
    {"id" : 6, "size" : "s", "color" : "yellow", "group" : "kids"},
    {"id" : 7, "size" : "m", "color" : "green", "group" : "kids"},
    {"id" : 8, "size" : "m", "color" : "blue", "group" : "kids"},
    {"id" : 9, "size" : "m", "color" : "red", "group" : "kids"},
    {"id" : 10, "size" : "m", "color" : "gray", "group" : "kids"},
    {"id" : 11, "size" : "m", "color" : "pink", "group" : "kids"},
    {"id" : 12, "size" : "m", "color" : "yellow", "group" : "kids"},
    {"id" : 13, "size" : "l", "color" : "green", "group" : "kids"},
    {"id" : 14, "size" : "l", "color" : "blue", "group" : "kids"},
    {"id" : 15, "size" : "l", "color" : "red", "group" : "kids"},
    {"id" : 16, "size" : "l", "color" : "gray", "group" : "kids"},
    {"id" : 17, "size" : "l", "color" : "pink", "group" : "kids"},
    {"id" : 18, "size" : "l", "color" : "yellow", "group" : "kids"}
]
app = FastAPI(title="FastAPI app",
              description="python project with fastAPI",
    summary="Practice project with python and fastAPI",
    version="0.0.1") #fastAPI constructor is called with arguments here


@app.get("/")
async def welcome(name : str):
    """Returns a friendly welcome message!"""
    return {"message": f"Hello World, welcome to this app, {name.upper()}!"}

@app.get("/date")
async def date():
    """Returns current time!"""
    return {"date" : datetime.datetime.now()}

@app.get("/api/shirts")
#async def getShirt(size: Optional[str] = None, color: Optional[str] =None) -> list:
def getShirt(size: str|None = None, color: str|None =None) -> List:
    result = dataBase
    if size:
        result = [car for car in result if car ['size'] == size]
    if color:
        result = [car for car in result if car ['color'] == color]
    return result


@app.get("/items/{id}")
def item_by_id(id : int) -> dict:
    result = [car for car in dataBase if car ['id'] == id]
    if (result):
        return result
    else:
        raise HTTPException(status_code=404, detail=f"No Shirt with the id= {id} found!")

if __name__ == "__main__":
    print("this function is called without being imported.")
    uvicorn.run("main:app", reload=True)