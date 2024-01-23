from fastapi import FastAPI
from models.models import Feedback

app = FastAPI()

# Пример пользовательских данных (для демонстрационных целей)
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

feedback = []
# Конечная точка для получения информации о пользователе по ID
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}

@app.get("/users/")
async def read_users(limit: int = 10):
    return dict(list(fake_users.items())[:limit])


@app.post('/feedback')
async def post_feedbeck(post: Feedback):
    feedback.append({post.name: post.message})
    return {"message": f"Feedback received. Thank you, {post.name}!"}