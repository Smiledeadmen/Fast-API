from fastapi import FastAPI
from models.models import User

app = FastAPI()
user = User(name='John Doe', id=1)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# новый роут
@app.get("/users", response_model=User)
def ger_users():
    return user