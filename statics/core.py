# -*- coding: utf-8 -*-
"""
    statics.extensions
    ~~~~~~~~~~~~~~

    Extensions module. Each extension is initialized in the app factory located
    in app.py

    https://github.com/sloria/cookiecutter-flask/blob/master/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/app.py
"""
from flask import Flask

from statics.extensions import flatpages, freezer
from statics.settings import ProdConfig
from statics import views


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(views.bp)
    return None


def register_extensions(app):
    flatpages.init_app(app)
    freezer.init_app(app)
    return None