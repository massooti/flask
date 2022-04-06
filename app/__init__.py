from flask import Flask
from app.routes import mainRoutes
from config import Config
app = Flask(__name__)

app.config.from_object(Config)
print(app.config["DATABASE"])
# db.init_app
# Register blueprint(s)
app.register_blueprint(mainRoutes)
# app.register_blueprint(xyz_module)

# db.create_all()
# ..
