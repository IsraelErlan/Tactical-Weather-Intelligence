import requests
from fastapi import HTTPException

def send_data_to_server_c(data: list):
    try:
        requests.post(url='http://localhost/8001/records', jsom=data)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise e
        