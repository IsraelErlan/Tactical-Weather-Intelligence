import requests
from fastapi import HTTPException

def send_data_to_server_c(data: list[dict]):
    try:
        print(000000000000)
        response = requests.post(url='http://localhost:8001/records', json=data)
        response.raise_for_status()
        return response.json()
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise e
        