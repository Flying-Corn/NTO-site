from flask import render_template, redirect, url_for

from . import app


@app.route('/')
def index():
    data = {}
    return render_template('index.html', data=data)


@app.errorhandler(404)
def error_404(e):
    return 'Ошибка! Страница не найдена'


@app.errorhandler(401)
def error_401(e):
    return redirect(url_for('/'))
