from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")


@app.get("/items/{type}/{item_id}", tags=["items"], response_class=FileResponse)
async def obtain_assets(type: str, item_id: str):
    return f"../static/{type}/{item_id}"
