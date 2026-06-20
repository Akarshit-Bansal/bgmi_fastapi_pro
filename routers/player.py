from fastapi import APIRouter
from datetime import datetime
from database import matches
from schemas import MatchRequest

router = APIRouter(prefix="/api/player", tags=["Player"])

@router.post("/match")
def add_match(data:MatchRequest):
    doc = data.model_dump()
    doc["created_at"] = datetime.utcnow()
    result = matches.insert_one(doc)
    return {"id":str(result.inserted_id),"message":"Match saved"}

@router.get("/leaderboard")
def leaderboard():
    pipeline=[
        {"$group":{"_id":"$playerId","kills":{"$sum":"$kills"}}},
        {"$sort":{"kills":-1}},
        {"$limit":10}
    ]
    return list(matches.aggregate(pipeline))
