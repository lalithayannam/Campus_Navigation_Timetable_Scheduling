
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api import router

app = FastAPI(
    title="Intelligent Campus Navigation and Scheduling System",
    version="1.0.0",
    description="Computational Thinking course project",
)

# Register API endpoints
app.include_router(router)

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND = BASE_DIR / "frontend"

# Serve CSS and JavaScript files
app.mount(
    "/static",
    StaticFiles(directory=str(FRONTEND)),
    name="static",
)

# Serve the main webpage
@app.get("/")
def index() -> FileResponse:
    return FileResponse(FRONTEND / "index.html")
