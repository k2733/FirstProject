
import config
from flask import Flask,jsonify, render_template,url_for,request,redirect
import pymssql

from sqlalchemy import Column,String,INT
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 

app = Flask(__name__)
app.config.from_object(config)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:vcc2022!@localhost/vcc'#(替换成自己的用户名，密码和dsn）

conn = pymssql.connect(host='VPC2201010',  port='1433', user='sa', password='vcc2022!', database='vcc')

# conn = pymssql.connect('VPC2201010','sa','vcc2022!','vcc')

cursor = conn.cursor()

# 新建、插入操作
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# 如果没有指定autocommit属性为True的话就需要调用commit()方法
conn.commit()

cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)