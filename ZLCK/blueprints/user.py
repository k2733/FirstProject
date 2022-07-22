from flask import Blueprint, render_template, request,redirect, url_for,session,flash
from exts import mail,db
from flask_mail import Message
from models import EmailCaptchaModel,UserModel
import string
import random
from datetime import datetime
from .forms import RegisterForm
from werkzeug.security import generate_password_hash  #生成密码哈希

bp = Blueprint("user",__name__,url_prefix='/user')

@bp.route('/login')
def login():
    return render_template("login.html")

@bp.route('/register',methods=['GET','POST'])
def register():
    
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate:
            email = form.email.data
            username = form.username.data
            password = form.password.data
            
            hash_password = generate_password_hash(password)  #生成一个密码对应的哈希
            
            user = UserModel(email=email,username=username,password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            # return redirect(url_for("user.register"))
            return "未能验证成功！"

#可以将验证码存储在memcached/redis/数据库中

@bp.route('/captcha')
def get_captcha():
    email = request.args.get("email")
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters,4))
    if email:
        message = Message(
            subject='邮箱测试',
            recipients=[email],
            body="【知乎】您的注册验证码是：%s.请不要告诉任何人哦！"  %captcha
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCaptchaModel(email = email,captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        print("captcha: ",captcha)
        return "success"
    else:
        return "没有输入邮箱"