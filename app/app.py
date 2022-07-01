from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import O_Data 

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
            error_msg = "username or password is wrong"
    else:
        error_msg = 'need username and password'

    return render_template('login.html', error_msg = error_msg)


@app.route('/list/')
def userlist():
    userlist = O_Data.read_data().items()
    print('userlist:%s' % userlist)
    return render_template('list.html', userlist = userlist)

@app.route('/update/')
def update():
    username = request.args.get('username')
    password = O_Data.read_data.get(username)
    user = [username, password]
    print('update:%s' % user)
    return render_template('update.html', user = user)

@app.route('/updateaction/', methods = ['POST'])
def updateaction():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username')
    password = params.get('password')
    O_Data.file_dict[username] = password
    O_Data.updata_data(username,password)
    return redirect('/list/')

#其他功能
if __name__ == '__main__':
    app.run()