from flask import Blueprint, request, render_template

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET', 'POST'])
def render_home():
    if request.method == 'POST':
        username = request.form['userName']
        username = str(username)
        password = request.form['userPassword']
        password = str(password)
        print(username + " " + password)
    return render_template('index.html')