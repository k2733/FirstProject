from multiprocessing import context
import config
from flask import Flask,jsonify, render_template,url_for,request,redirect


app = Flask(__name__)
app.config.from_object(config)

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/about')
def about():
    context = {'username':'周杰伦',
                'books': ['红楼梦','水浒传']
    }

    return render_template('about.html',**context)

@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)