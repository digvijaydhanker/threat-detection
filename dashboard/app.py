from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import numpy as np
hostname = 'localhost'
database = 'employeeDB'
username = 'postgres'
pwd = 'admin'
port_id = 5432
conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id)
cur = conn.cursor()
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABAE_URI']='postgresql://postgres:admin@localhost/employeeDB'
# db = SQLAlchemy(app)



@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/contextget', methods=['GET']) 
def contextget():
    sql_query ="""SELECT * FROM employee WHERE name='Tim'"""
    out = cur.execute(sql_query)
    context_records = cur.fetchall() 
    ContextRootKeys = []
    outp ="Print each row and it's columns values"
    for row in context_records:
        ContextRootKeys.append(row[2])
    
    conn.commit()
    print(ContextRootKeys[0])
    return outp

@app.route('/analytics/<id>', methods=['GET']) 
def analytics(id):
    sql_query ="""SELECT * FROM employee WHERE location=%s"""
    var = (id,)
    out = cur.execute(sql_query,var)
    context_records = cur.fetchall() 
    ContextRootKeys = []
    for row in context_records:
        ContextRootKeys.append(row[2])
    
    conn.commit()
    leny = len(ContextRootKeys[0])
    x = np.arange(start=1, stop=leny+1, step=1)
    list1 = x.tolist()
    print(list1)
    return render_template("employee.html", name=id, data=ContextRootKeys[0],xaxis=list1)
if __name__ == '__main__':
    app.run(debug=True)