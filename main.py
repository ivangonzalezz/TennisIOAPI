from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from typing import List, Union
from datetime import datetime
from pydantic import BaseModel
import json

class Movement(BaseModel): 
    identifier: Union[str, None] = None
    kind: Union[str, None] = None 
    pitch: Union[float, None] = None
    roll: Union[float, None] = None
    yaw: Union[float, None] = None
    timestamp: Union[str, None] = None
    xAcceleration: Union[float, None] = None
    yAcceleration: Union[float, None] = None
    zAcceleration: Union[float, None] = None
    xRotation: Union[float, None] = None
    yRotation: Union[float, None] = None
    zRotation: Union[float, None] = None
    
    

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadMovements/")
async def upload_movements(movements: List[Movement]):
    trainment_date = datetime.strptime(movements[0].identifier, "%d-%m-%Y %H:%M:%S")
    filename = "trainments/{}.json".format(datetime.strftime(trainment_date, "%Y%m%d_%H%M%S"))
    with open(filename, 'w') as f:
        json_data = jsonable_encoder(movements)
        json.dump(json_data, f)
    return {"movements": True}
