from flask import Flask, request, render_template
from Routes import Login
import psycopg2
import pandas as pd

app = Flask(__name__)

#conn = psycopg2.connect(host='localhost', dbname='mydb',user='postgres', password=1234, port='5432')

#커서 만들기
#커서 객체는 실질적으로 DB에 쿼리문을 수행하고, 결과를 가져오는 역할
#cur = conn.cursor()

#쿼리문 수행
#cur.execute('SELECT * FROM public.f1_fasoo')
#info = cur.fetchall()

#cur.close()
#conn.close()

@app.route('/', methods=['GET', 'POST'])
def render_home():
    if request.method == 'POST':
        username = request.form['userName']
        username = str(username)
        password = request.form['userPassword']
        password = str(password)
        print(username + password)
    return render_template('index.html')

@app.route('/book')
def render_book():
    return '예약하기'

@app.route('/book/check')
def render_book_check():
    return '결제하기'

if __name__ == '__main__':
    app.run(debug=True)