from fastapi import FastAPI
from fastapi .staticfiles import StaticFiles
from routers import index
app = FastAPI()

app.include_router(index.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)