from flask import Flask
from config import Config
from app.routes.api import mainRoutes

# from .app.controllers import *
# from .app.models import *
import config

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(mainRoutes)
# app.init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089, debug=True)
