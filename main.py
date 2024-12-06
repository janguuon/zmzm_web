from fastapi import FastAPI
from routers import index, login, join
app = FastAPI()

app.include_router(index.router)
app.include_router(login.router)
app.include_router(join.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)