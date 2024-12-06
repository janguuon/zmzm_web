from fastapi import FastAPI, APIRouter, Request
from fastapi .templating import Jinja2Templates
from fastapi .responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/join", response_class=HTMLResponse)
async def login_Page(request: Request):
    return templates.TemplateResponse("join.html", context={"request":request})