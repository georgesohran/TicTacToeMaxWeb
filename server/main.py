from fastapi import FastAPI, WebSocket

app = FastAPI()



@app.get('/')
def get1():
    return {'title': 'hello world'}


app.websocket('/ws')
async def ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send({

        })