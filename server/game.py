from fastapi import WebSocket, WebSocketDisconnect
import random


class GameField:
  def __init__(self, heigth: int, width: int):
    self.fields = [[''] * width] * heigth
  
  def mark(self, x: int, y: int, sign: str):
    self.fields[x][y] = sign
  
  def serialize(self):
    return self.fields



class GameRoom:
  def __init__(self, game_params: dict):
    self.players: list[WebSocket] = []
    self.max_players: int = game_params.pop('max_players')
    self.game_field: GameField = GameField(**game_params)

  async def connect(self, websocket: WebSocket):
    await websocket.accept()
    if len(self.players) <= self.max_players:
      self.players.append(websocket)

  async def send_game_data(self):
    for player in self.players:
      await player.send_json(self.game_field.serialize()) 



class GameManeger:
  def __init__(self):
    self.active_games: dict[int, GameRoom] = {}
  
  def create_game(self, game_params: dict[str, str|int|bool]):
    game = GameRoom(game_params) 
    self.active_games[len(self.active_games)+1] = game
    return len(self.active_games) + 1
  
