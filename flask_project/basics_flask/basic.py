from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Welcome to flask</h1>"

@app.route('/information')
def info():
    return "<h1>information View</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "Puppy name is {}".format(name)

if __name__ == '__main__':
    app.run(debug=True)