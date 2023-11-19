from fastapi import FastAPI, HTTPException
from schemas import load_db, save_db, save_new, ShirtInput, ShirtOutput
import datetime
import uvicorn
from typing import List
from typing import Dict

app = FastAPI(title="FastAPI Shirt app",
              description="python project with fastAPI",
    summary="Practice project with python and fastAPI",
    version="0.0.1") #fastAPI constructor is called with arguments here
dataBase = load_db()

@app.get("/")
async def welcome(name : str):
    """Returns a friendly welcome message!"""
    return {"message": f"Hello World, welcome to this app, {name.upper()}!"}

@app.get("/date")
async def date():
    """Returns current time!"""
    return {"date" : datetime.datetime.now()}

@app.get("/api/shirts") #query prameter
#async def getShirt(size: Optional[str] = None, color: Optional[str] =None) -> list:
def get_shirt(size: str|None = None, color: str|None =None) -> List: #type hints
    result = dataBase
    if size:
        result = [shirt for shirt in result if shirt.size == size]
    if color:
        result = [shirt for shirt in result if shirt.color == color]
    return result


@app.get("/items/{id}") #path parameter
def item_by_id(id : int) -> dict:
    #print (dataBase)
    result = [shirt for shirt in dataBase if shirt.id == id]
    if result:
        print ("result")
        print (result[0].model_dump())
        return result[0].model_dump()
    else:
        raise HTTPException(status_code=404, detail=f"No Shirt with the id= {id} found!")

@app.post("/api/shirts", response_model=ShirtOutput) #declaring return type here used to work and it still does
def add_shirt(shirt: ShirtInput) -> ShirtOutput: #Specifying(type hinting) the output ddidn't used to do anything here
    new_shirt = ShirtOutput(size=shirt.size, 
                            color=shirt.color,
                            id=len(dataBase) + 1,
                            group=shirt.group)
    dataBase.append(new_shirt)
    save_new(new_shirt)
    save_db(dataBase)
    return(new_shirt)

#A 204 status code is used when the server successfully processes the request,
#  but there is no content to return to the client.
@app.delete("/items/{id}", status_code=204)
def remove_shirt(id: int) -> None:
    matches = [shirt for shirt in dataBase if shirt.id == id]  
    if matches:
        shirt =matches[0]
        dataBase.remove(shirt)
        save_db(dataBase)
    else:
        raise HTTPException(status_code=404, detail=f"No shirt with that id={id}.")

@app.put("/api/shirts/{id}", response_model=ShirtOutput)
#new_shirt is a pydantic object that will come with the request's body
def change_shirt(id: int, new_shirt: ShirtInput) -> ShirtOutput:
    matches = [shirt for shirt in dataBase if shirt.id == id]  
    if matches:
        shirt = matches[0]
        shirt.color = new_shirt.color
        shirt.size = new_shirt.size
        shirt.group = new_shirt.group
        save_db(dataBase)
        return shirt
    else:
        raise HTTPException(status_code=404, detail=f"No shirt with that id={id}.")

if __name__ == "__main__":
    print("this function is called without being imported.")
    uvicorn.run("main:app", reload=True)