from flask import Flask

def create_app():
    from routes import home
    app = Flask(__name__)
    app.register_blueprint(home)
    return app