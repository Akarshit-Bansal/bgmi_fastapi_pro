from jose import jwt
import os

def create_token(user_id:str):
    return jwt.encode({"id": user_id}, os.getenv("JWT_SECRET"), algorithm="HS256")
