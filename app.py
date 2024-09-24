from flask import Flask
from controllers.file_controller import file_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(file_blueprint)
    return app
