import json
from models.calculator import calculator
from flask import Flask, render_template, url_for, redirect, jsonify, request
from wtforms import Form, FloatField, validators,IntegerField
import mysql.connector
import time
from datetime import datetime

mydb = mysql.connector.connect(user = 'root',
                               host = 'localhost',
                              database = 'tnq_flask')
app = Flask(__name__, static_url_path='/static')



class InputForm(Form):
    A = IntegerField(
        label='A', default=0,
        validators=[validators.InputRequired()])
    b = IntegerField(
        label='B', default=0,
        validators=[validators.InputRequired()])




@app.route("/", methods=['GET', 'POST'])
def home():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        req_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ip_addr = request.remote_addr
        start_time = time.time()
        result = calculator()._compute(form.A.data, form.b.data)
        mycursor = mydb.cursor()
        sql = "INSERT INTO tnq_datas (Addition,Subtraction,Multiplication,Divsion) VALUES (%s, %s,%s, %s)"
        val = tuple(result.values())
        #val = (values)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        processt = time.time() - start_time
        result['IP address'] = ip_addr
        result['Requested time'] = req_time
        result['process time'] = str(round(processt,2))+" seconds"
    else:
        result = None

    return render_template("index.html",form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
