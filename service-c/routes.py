from fastapi import APIRouter, HTTPException
from sql_manager import SQLManager
import mysql.connector
def get_connection(): pass
router = APIRouter()

@router.get('/records/count')
def get_records(): 
    try:
        conn = get_connection()
        data = SQLManager.get_records(conn)
        return data
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="database connection error")
    

@router.get('/records/count')
def get_count_records_by_area():
    try:
        conn = get_connection()
        data = SQLManager.get_count_records_by_area(conn)
        return data
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="database connection error")
    

@router.get('/records/avg-temperature')
def get_avg_temperature_by_area():
    try:
        conn = get_connection()
        data = SQLManager.get_avg_temperature_by_area(conn)
        return data
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="database connection error")
    

@router.get('/records/max-wind')
def get_max_wind_by_area():
    try:
        conn = get_connection()
        data = SQLManager.get_max_wind_by_area(conn)
        return data
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="database connection error")
    

@router.get('/records/extreme')
def get_extreme_locations():
    try:
        conn = get_connection()
        data = SQLManager.get_extreme_locations(conn)
        return data
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="database connection error")