from fastapi import APIRouter, Request
from fastapi .templating import Jinja2Templates
from fastapi .responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/login", response_class=HTMLResponse)
async def login_Page(request: Request):
    return templates.TemplateResponse("login.html", context={"request":request})