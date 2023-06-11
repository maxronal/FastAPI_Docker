from fastapi import FastAPI
import random
from os import environ as env

app = FastAPI(title="RandomId_App",
    description="APP RandomId",
    version="0.0.1",
    contact={
        "name": "Max Ronal",
        "email": "ronallaurenteb@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    })

@app.get("/")
def index():
    return {"Index": f"OK {env['MY_VARIABLE']}"}

@app.get("/randomId/{id}")
def get_number(id:int):
    ran_a=random.randint(1,10)
    return {"id":f"{str(id)}",
            "Random":f"{ran_a}",
            "output": f" {id*2022 + ran_a} "}