from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse

page = 'index.html'
app = FastAPI()


@app.get("/")
async def root():
    return FileResponse(page)

@app.post('/calculate')
async def calc(num1: int, num2: int):
    return JSONResponse({'result': num1 + num2})

