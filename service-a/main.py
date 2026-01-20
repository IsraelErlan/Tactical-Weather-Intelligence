import uvicorn
from fastapi import FastAPI
from api_extractor import get_data
from schames import Location

app = FastAPI()

@app.post("/ingest")
def get_locations(location: Location):
    return get_data(location.locations)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",port=8000 , reload=True)
