from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Root!</p>"

@app.route('/index')
def index():
    return render_template('index.html') # templatesフォルダ内のindex.htmlを表示する

