from fastapi import APIRouter, HTTPException
from data_handler import WeatherData
from api_request import send_data_to_server_c

router = APIRouter()


@router.post('/clean')
def clean_data(weather_list: list[dict]):
    try:
        data = WeatherData.create_and_run(weather_list)
        res = send_data_to_server_c(data)
        return res
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        status = getattr(e, "status_code", 500)
        msg = getattr(e, "detail", getattr(e, "message", str(e)))
        raise HTTPException(status_code=status, detail=msg)
    