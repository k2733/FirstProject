from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://C##VCC:VCC@dx.huangyi.cn:1521/ORCL'
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello,Flask!'

@app.route('/login')
def login():
    return '登录逻辑'


#其他功能
if __name__ == '__main__':
    app.run()