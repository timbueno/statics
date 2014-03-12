# -*- coding: utf-8 -*-
"""
    statics.views
    ~~~~~~~~~~~~~~

    Views module that contains the 'views' blueprint that handles
    all basic endpoints
"""
from flask import current_app, Blueprint, render_template

from . import route
from .extensions import flatpages


bp = Blueprint('views', __name__)

@route(bp, '/')
def index():
    """On the index page, show a list of blog posts"""
    posts = [p for p in flatpages if p.path.startswith(current_app.config['POST_DIR'])]
    return render_template('index.html', posts=posts)

@route(bp, '/pages/<name>/')
def page(name):
    """For non-blogpost pages, e.g. About, Contact, etc..."""
    path = '{}/{}'.format(current_app.config['PAGE_DIR'], name)
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)

@route(bp, '/posts/<name>/')
def post(name):
    """For blogpost type pages"""
    path = '{}/{}'.format(current_app.config['POST_DIR'], name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)