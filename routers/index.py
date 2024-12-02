from fastapi import FastAPI, APIRouter, Request
from fastapi .templating import Jinja2Templates
from fastapi .responses import HTMLResponse

router = APIRouter()
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index_Page(request: Request):
    return templates.TemplateResponse("index.html", context={"request":request})

@router.get("/login", response_class=HTMLResponse)
async def login_Page(request: Request):
    return templates.TemplateResponse("login.html", context={"request":request})