from flask_sqlalchemy import SQLAlchemy
from exts import db
from sqlalchemy.orm import relationship

#创建ORM模型
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)
    
    #外键：
    #1.外键的数据类型要看所引用的数据类型
    #2.db.ForeignKey("表名.字段名")
    #3.外键是数据数据库层面的，不推荐在ORM中直接使用
    author_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    #relationship:
    #1.第一个参数是模型的名字，必须和模型名字保持一致
    #2.backref(back reference):代表反向引用，代表对方访问我的时候的字段名称
    author = db.relationship("Users",backref="articles")


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200),nullable=False)
