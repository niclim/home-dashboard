from flask import Flask

from home_dashboard.routes import routes


def create_app(is_testing=False):
    app = Flask(__name__)

    app.register_blueprint(routes)

    return app
