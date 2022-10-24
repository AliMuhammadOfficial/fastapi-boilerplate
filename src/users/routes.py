from fastapi import APIRouter

users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.get("/")
async def fetch_users():
    return {
        "data": [
            {"name": "John Doe", "email": "john@example.com"}
        ]
    }

@users_router.post("/")
async def create_user():
    return {"message": "User Created"}

@users_router.put("/")
async def update_user():
    return {"message": "User Updated"}