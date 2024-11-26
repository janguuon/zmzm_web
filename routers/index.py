from fastapi import FastAPI, APIRouter, Request
from fastapi .templating import Jinja2Templates
from fastapi .responses import HTMLResponse
import os

router = APIRouter()
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index_Page(request: Request):
    return templates.TemplateResponse("index.html", context={"request":request})

@router.post("/dir/test")
async def test():
    print("시작")
    text='test시작'
    return text

# bp = Blueprint('home', __name__)

# @bp.route('/', methods=['GET', 'POST'])
# def render_home():
#     if request.method == 'POST':
#         username = request.form['userName']
#         username = str(username)
#         password = request.form['userPassword']
#         password = str(password)
#         print(username + " " + password)
#     return render_template('index.html')