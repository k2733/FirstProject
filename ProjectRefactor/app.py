
from flask import Flask, Response, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from models import Users,Article
from exts import db

app = Flask(__name__)
app.config.from_object(config)
#把app绑定到db上
db.init_app(app)

migrate = Migrate(app,db)


#设置cookie
@app.route('/set_cookie')
def set_cookie():
    response = Response('cookie 设置')
    response.set_cookie("user_id","xxx")
    return response

#获取cookie
@app.route('/get_cookie')
def get_cookie():
    user_id = request.cookies.get("user_id")
    print("user_id: ",user_id)
    return "获取cookie"

#设置session
@app.route('/set_session')
def set_session():
    session['username'] = 'zhiliao'
    return "session设置成功"


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/otm')
def one_to_many():
    #orm模型一对多关系
    artcile1 = Article(title='111',content='xxx') 
    artcile2 = Article(title='222',content='yyy')
    user = Users(username = '常州')
    artcile1.author = user
    artcile2.author = user
    db.session.add(artcile1,artcile2)
    db.session.commit()

    return "one to many数据操作成功"

if __name__ == '__main__':
    app.run(debug=True)