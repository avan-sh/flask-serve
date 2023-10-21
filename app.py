from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates',static_folder='./static')

@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/')
@app.route('/hello/<name>')
@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)