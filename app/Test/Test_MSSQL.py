#coding:utf-8
from sqlalchemy import table
import MSSQL
from flask import Flask,render_template,request,redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/loginaction/', methods = ["POST","GET"])
def login():
    error_msg = ''
    
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

    print('username:%s,password:%s' % (username,password))

    if username and password:
        if username == "admin" and password == "admin":
            return redirect('/list')
        else:
            error_msg = "账户不存在或密码错误!!!"
    else:
        error_msg = '请输入账号和密码！'

    return render_template('login.html', error_msg = error_msg)

@app.route('/list/')
def table_list():
    sql = 'select * from persons'
    ms=MSSQL.SqlsvLib()
    table_search = ms.ExecSqlQuery(sql)
    return render_template('list.html', table_list = table_search)

@app.route('/update/')
def update():
    iid = request.args.get('id')
    username = request.args.get('username')
    password = request.args.get('password')
    list = [iid,username,password]
    return render_template('update.html', table_list = list)


@app.route('/updateaction/', methods = ['POST'])
def updateaction():
    params = request.args if request.method == 'GET' else request.form
    iid = int(params.get('id_number'))
    username = str(params.get('username'))
    password = str(params.get('password'))
    sql = "updata persons set name = '%s',password= '%s' where id=%d" %(username,password,iid)
    ms=MSSQL.SqlsvLib()
    ms.ExecNonQuery(sql)
    return redirect('/list/')


@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addaction/', methods = ['POST'])
def addaction():
    params = request.args if request.method == 'GET' else request.form
    iid = params.get('id_number')
    username = params.get('username')
    password = params.get('password')

    ms=MSSQL.SqlsvLib()
    sql = 'select * from persons'
    table_search = ms.ExecSqlQuery(sql)

    if username in {i[1] for i in table_search}:
        return redirect('/list/')
    else:
        sql = "insert into persons values(%d,'%s','%s')" %(int(iid),username,password)
        ms=MSSQL.SqlsvLib()
        table_search = ms.ExecNonQuery(sql) 
        # Test_MSSQL_D.MSSOL_add(sql)
        return  redirect('/list/')

@app.route('/delete/')
def delete():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username')
    sql = "delete from persons where name = '%s'"  %(username)
    ms=MSSQL.SqlsvLib()
    aa = ms.ExecNonQuery(sql)
    return redirect('/list/')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)