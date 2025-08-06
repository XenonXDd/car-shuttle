from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import csv
import os


app = FastAPI()

# Mount the static directory to serve CSS, JS, images etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

PASSENGERS_CSV = "data/passengers.csv"
DRIVERS_CSV = "data/drivers.csv"


class Passenger(BaseModel):
    id: str
    username: str
    password: str


class Driver(BaseModel):
    id: str
    username: str
    password: str


def write_to_csv(file_path, data):
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["id", "username", "password"])
        writer.writerow(data)


def read_csv_by_id(file_path, record_id):
    with open(file_path, mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["id"] == record_id:
                return row
    return None

# Serve the index.html file from static folder at root "/"
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/register-passenger")
def register_passenger(passenger: Passenger):
    # Check if ID already exists to avoid duplicates
    if read_csv_by_id(PASSENGERS_CSV, passenger.id):
        raise HTTPException(status_code=400, detail="Passenger ID already exists")
    write_to_csv(PASSENGERS_CSV, [passenger.id, passenger.username, passenger.password])
    return {"message": "Passenger registered", "id": passenger.id}


@app.post("/register-driver")
def register_driver(driver: Driver):
    if read_csv_by_id(DRIVERS_CSV, driver.id):
        raise HTTPException(status_code=400, detail="Driver ID already exists")
    write_to_csv(DRIVERS_CSV, [driver.id, driver.username, driver.password])
    return {"message": "Driver registered", "id": driver.id}


@app.get("/passenger-info/{passenger_id}")
def get_passenger_info(passenger_id: str):
    result = read_csv_by_id(PASSENGERS_CSV, passenger_id)
    if not result:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return result


@app.get("/driver-info/{driver_id}")
def get_driver_info(driver_id: str):
    result = read_csv_by_id(DRIVERS_CSV, driver_id)
    if not result:
        raise HTTPException(status_code=404, detail="Driver not found")
    return result


@app.get("/match-passengers-to-drivers")
def match_passengers_to_drivers():
    # Placeholder logic for matching
    return {"message": "Matching algorithm not implemented yet"}
