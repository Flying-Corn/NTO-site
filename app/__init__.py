from flask import Flask

# app = Flask(__name__, template_folder='../templates', static_folder='../templates/static')
app = Flask(__name__, template_folder='templates', static_folder='templates/static')
# app = Flask(__name__)
app.config.from_object('config.Config')

from .views import app
