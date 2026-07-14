import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from db import fetch_one

app = FastAPI(title="Ye Jeong Park - Solar Forecast Dashboard")


@app.get("/api/health")
def health():
    try:
        row = fetch_one("SELECT NOW() AS now")
        return {"status": "ok", "db_time": row["now"]}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"DB connection failed: {exc}")


@app.get("/")
def index():
    return FileResponse("index.html")


app.mount("/static", StaticFiles(directory="."), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
