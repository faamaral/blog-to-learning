from flask import Flask

def create_app(config_settings):
    app = Flask(__name__)

    return app