from flask import Flask
from config import Config
from src.routes._api import mainRoutes
from src.models.Database import Database

app = Flask(__name__)
app.register_blueprint(mainRoutes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089, debug=True)
