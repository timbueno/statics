# -*- coding: utf-8 -*-
"""
    statics.settings
    ~~~~~~~~~~~~~~

    Settings are devided into two classes, production and development
"""
import os


class Config(object):
    """Configuration baseclass"""
    SECRET_KEY = 'RD8kARq4ZcXrdck'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Flask-FlatPages Settings
    FLATPAGES_ROOT = '../content'
    FLATPAGES_EXTENSION = '.md'
    POST_DIR = 'posts'
    PAGE_DIR = 'pages'
    SITE_NAME = 'Tim Bueno\'s Blog'

    # Frozen-Flask Settings
    FREEZER_IGNORE_MIMETYPE_WARNINGS = True
    FREEZER_RELATIVE_URLS = True
    FREEZER_DESTINATION = '../build'


class ProdConfig(Config):
    """Production configuration"""
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration"""
    ENV = 'dev'
    DEBUG = True