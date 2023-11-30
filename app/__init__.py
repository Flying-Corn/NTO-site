from flask import Flask

app = Flask(__name__, template_folder='../docs', static_folder='../docs/static')
app.config.from_object('config.Config')

from .views import app
