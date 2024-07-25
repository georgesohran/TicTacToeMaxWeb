from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from game import *

app = FastAPI()
game_manager = GameManeger()



@app.post('/game')
def create_game(data):
  game_params = data['game_params']
  id = game_manager.create_game(game_params)
  return {'detail': 'success', 'game':game_manager.active_games[id]}


@app.websocket('game/{room_id}/{client_id}')
async def ws(websocket: WebSocket, room_id:str, client_id:str):
  await websocket.accept()
  while True:
    data = await websocket.receive_json()
    await websocket.send({
      
      })