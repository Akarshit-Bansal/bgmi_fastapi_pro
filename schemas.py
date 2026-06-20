from pydantic import BaseModel

class RegisterRequest(BaseModel):
    username:str
    password:str

class LoginRequest(BaseModel):
    username:str
    password:str

class MatchRequest(BaseModel):
    playerId:str
    kills:int
    position:int
