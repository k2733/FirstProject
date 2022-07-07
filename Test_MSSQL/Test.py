#coding:utf-8
#! 使用sqlalchemy操作数据库
# from ast import With
# import imp

# from flask_sqlalchemy import SQLAlchemy
# import MSSQL
# from flask import Flask
# from sqlalchemy import create_engine

# #数据库配置参数
# HOSTNAME = 'VPC2201010'
# PORT = '1433'
# DATEBASE = 'vcc'
# USENAME = 'sa'
# PASSWORD = 'vcc2022!'

# #创建SQL Server数据库引擎 。如果是要创建mysql的引擎，前缀部分应该改为：'mysql+mysqldb:' , 如果是连接oracle,前缀改为 'oracle+cx_Oracle:' 即可；
# DB_URI = 'mssql+pymssql://{}:{}@{}:{}/{}' .format(USENAME,PASSWORD,HOSTNAME,PORT,DATEBASE)
# engine = create_engine(DB_URI)

# #创建连接
# with engine.connect() as con:
#     rs = con.execute('select * from persons')
#     print (rs.fetchall())



#! flask-sqlalchemy的使用
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

HOSTNAME = 'VPC2201010'
PORT = '1433'
DATEBASE = 'vcc'
USENAME = 'sa'
PASSWORD = 'vcc2022!'

DB_URI = 'mssql+pymssql://{}:{}@{}:{}/{}' .format(USENAME,PASSWORD,HOSTNAME,PORT,DATEBASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

#创建ORM模型
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)

# db.create_all()

migrate = Migrate(app,db)

#*（在终端输入，并非在脚本中）
#flask db init                  初始化迁移库
#flask db migrate -m '备注'     创建迁移脚本
#flask db upgrade               提交迁移命令，使迁移脚本生效

@app.route('/article')
def article_view():
    # 1.添加数据
    # article = Article(title='钢铁是怎样炼成的',content='xxx')
    # db.session.add(article)
    # db.session.commit()


    # 2.查询数据
    # filter_by 返回的是一个类列表的对象
    # article = Article.query.filter_by(id=1)[0]
    # print(article.title)

    # 3.修改数据
    # article = Article.query.filter_by(id=1)[0]
    # article.content='yyy'
    # db.session.commit()

    #4.删除数据
    # Article.query.filter_by(id=1).delete()
    # db.session.commit()

    return '数据操作成功！'


@app.route('/')
def hello_world():
    # engine = db.get_engine()
    # with engine.connect() as conn:
    #     result = conn.execute('select * from persons')
    #     print(result.fetchall())
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)


#!使用pymssql操作sql server数据库（使用SQL语句操作）
# ms=MSSQL.SqlsvLib()
# ll=ms.ExecNonQuery("insert into persons values(4,'jake','jake.M')")
# ll=ms.ExecSqlQuery("select * from persons")
# print(ll)

# ms=MSSQL.SqlsvLib()
# password='dkk'
# username='akk'
# idd=2
# sql = "UPDATE persons set name = 'akk' where id =2 "
# aa = ms.ExecNonQuery(sql)