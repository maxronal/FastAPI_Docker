from fastapi import FastAPI
import random

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
    return {"Index": "OK"}

@app.get("/randomId/{id}")
def get_number(id:int):
    return {"output": f" {id*2022 + random.randint(1,10)} "}