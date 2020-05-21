from flask import Flask


def create_app(is_testing=False):
    app = Flask(__name__)

    return app
