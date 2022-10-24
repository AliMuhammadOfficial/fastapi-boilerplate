from fastapi import FastAPI
from src.auth.routes import auth_router
from src.users.routes import users_router
from src.config.config import app_name


app = FastAPI(title=app_name)

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/", tags=["Home"])
def home():
    return {"message": f"Hello {app_name}"}
