from flask import Flask
from config import Config
from src.routes.api import mainRoutes
from src.database.Database import Database
from src.database.seeder import UserSeeder
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "abcb45eebb824e9d8723adb8f6210acc"
jwt = JWTManager(app)

app.register_blueprint(mainRoutes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089, debug=Config.DEBUG)
