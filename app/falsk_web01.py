#coding:utf-8
import cx_Oracle
from flask import Flask,render_template,request,redirect
import fileutils
import config
# 引入file_dict用户列表
fileutils.file_read()

app = Flask(__name__)
app.config.from_object(config)

# tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")  #监听Oracle数据库
# conn = cx_Oracle.connect("C##VCC","VCC",tns)   #连接数据库

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
def userlist():
    userlist = fileutils.file_read().items()
    print('userlist:%s' % userlist)
    return render_template('list.html', userlist = userlist)

@app.route('/update/')
def update():
    username = request.args.get('username')
    password = fileutils.file_read().get(username)
    user = [username, password]
    print('update:%s' % user)
    return render_template('update.html', user = user)


@app.route('/updateaction/', methods = ['POST'])
def updateaction():
    params = request.args if request.method == 'GET' else request.form
    
    username = params.get('username')
    password = params.get('password')
    fileutils.file_dict[username] = password
    fileutils.file_write(username,password)
    return redirect('/list/')


@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addaction/', methods = ['POST'])
def addaction():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username')
    password = params.get('password')

    if username in fileutils.file_dict:
        return redirect('/list/')
    else:
        tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")  #监听Oracle数据库
        conn = cx_Oracle.connect("C##VCC","VCC",tns)   #连接数据库
        cursor = conn.cursor()
        sql = "insert into tb_user values('%s','%s')" %(username,password)
        try:
                cursor.execute(sql)
                conn.commit() 
                print("数据更新成功")
        except:
                conn.rollback() #发生错误时回滚
                print("语句执行错误")
        conn.close()
        return  redirect('/list/')

@app.route('/delete/')
def delete():
    username = request.args.get('username')
    # del fileutils.file_dict[username]
    # fileutils.file_dict.pop(username)
    tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")  #监听Oracle数据库
    conn = cx_Oracle.connect("C##VCC","VCC",tns)   #连接数据库
    cursor = conn.cursor()
    sql = "delete from tb_user where name = '%s'"  %username
    try:
            cursor.execute(sql)
            conn.commit() 
            print("数据更新成功")
    except:
            conn.rollback() #发生错误时回滚
            print("语句执行错误")
    conn.close()
    return redirect('/list/')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)