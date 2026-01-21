from fastapi import APIRouter, HTTPException
from data_handler import WeatherData

router = APIRouter()


@router.post('/clean')
def clean_data(weather_list: list[dict]):
    try:
        WeatherData.create_and_run(weather_list)
        return data
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        status = getattr(e, "status_code", 500)
        msg = getattr(e, "detail", getattr(e, "message", str(e)))
        raise HTTPException(status_code=status, detail=msg)
    