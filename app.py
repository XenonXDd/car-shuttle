from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the static directory at /static so CSS/JS/images are accessible
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set templates directory
templates = Jinja2Templates(directory="templates")

# Example route serving index.html
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Additional routes for other pages, e.g. registration forms

@app.get("/register-driver", response_class=HTMLResponse)
async def register_driver_page(request: Request):
    return templates.TemplateResponse("register-driver.html", {"request": request})

@app.get("/register-passenger", response_class=HTMLResponse)
async def register_passenger_page(request: Request):
    return templates.TemplateResponse("register-passenger.html", {"request": request})

@app.get("/dashboard-passenger", response_class=HTMLResponse)
async def dashboard_passenger_page(request: Request):
    return templates.TemplateResponse("dashboard-passenger.html", {"request": request})

@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# You can add more routes to serve other templates similarly
