from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar as rotas
    from .routes import app as routes_bp
    app.register_blueprint(routes_bp)

    return app
