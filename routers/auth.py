from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from database import users
from schemas import RegisterRequest, LoginRequest
from auth_utils import create_token

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/register")
def register(data:RegisterRequest):
    if users.find_one({"username":data.username}):
        raise HTTPException(400,"User already exists")
    result = users.insert_one({
        "username":data.username,
        "password":bcrypt.hash(data.password)
    })
    return {"id":str(result.inserted_id),"username":data.username}

@router.post("/login")
def login(data:LoginRequest):
    user = users.find_one({"username":data.username})
    if not user or not bcrypt.verify(data.password,user["password"]):
        raise HTTPException(401,"Invalid credentials")
    return {"token":create_token(str(user["_id"]))}
