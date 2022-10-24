from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/login")
async def login():
    return {"token": "you will receive token"}

@auth_router.post("/register")
async def register():
    return {"message": "user registration endpoint"}

@auth_router.get("/profile")
async def my_profile():
    return {"message": "My Profile"}