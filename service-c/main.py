import uvicorn
from fastapi import FastAPI
from storage_db import save_weather_records
from connection_db import init_connection_pool
from init_db import init_database
from routes import router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_database()  # create database
    init_connection_pool()  # create reservoir  of connections


@app.post("/records")
def save_to_db(data:list[dict]):
    return save_weather_records(data)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8001, reload=True)
