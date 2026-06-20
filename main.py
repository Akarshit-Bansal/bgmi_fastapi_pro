from fastapi import FastAPI, WebSocket
from routers.auth import router as auth_router
from routers.player import router as player_router

app = FastAPI(title="BGMI FastAPI Backend")

app.include_router(auth_router)
app.include_router(player_router)

@app.get("/")
def root():
    return {"status":"running"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_text("Player connected")
    while True:
        await ws.receive_text()
