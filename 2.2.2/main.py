from fastapi import FastAPI
from models.models import User
from starlette.responses import JSONResponse

app = FastAPI()


@app.post("/user")
async def show_user(usr: User):
    return {"name": usr.name,
            "age": usr.age,
            "is_adult": usr.age>=18}