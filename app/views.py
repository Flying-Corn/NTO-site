from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__, template_folder='../docs')
app.config.from_object('config.Config')


@app.route('/')
def index():
    data = {}
    return render_template('index.html', data=data)


@app.errorhandler(404)
def error_404(e):
    data = {}
    return render_template('index.html', data=data)


@app.errorhandler(401)
def error_401(e):
    return redirect(url_for('/'))
