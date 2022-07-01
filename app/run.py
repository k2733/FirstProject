
import config
from flask import Flask,jsonify,url_for,request,redirect


app = Flask(__name__)
app.config.from_object(config)

books = [
    {"ID":1,"name":'三国演义'},
    {"ID":2,"name":'甄嬛传'}
]

#从服务器获取数据，用GET请求
#从前端发送数据给服务器，用POST请求
# redirect() 重定向


@app.route("/book/<int:book_id>",methods=['GET'])
def book_detail(book_id):
    for book in books:
        if book_id == book['ID']:
            return book
    return f"id为: {book_id} 的图书没有找到"


@app.route("/book/list")
def booklist():
    for book in books:
        book['url']= url_for("book_detail",book_id=book['ID'])
    return jsonify(books)

@app.route("/profile")
def profile():
    user_id = request.args.get('id')
    if user_id:
        return "用户个人中心"
    else:
        return redirect(url_for("index"))

@app.route('/')
def index():
    return 'Hello!'


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)