from fastapi import FastAPI
from fastapi .staticfiles import StaticFiles
from routers import index
app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(index.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host='0.0.0.0', port=5000, reload=True)