from fastapi import APIRouter, Request
from fastapi .templating import Jinja2Templates
from fastapi .responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index_Page(request: Request):
    return templates.TemplateResponse("index.html", context={"request":request})