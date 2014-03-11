# -*- coding: utf-8 -*-
"""
    statics
    ~~~~~~~~~~~~~~

    Statics application package
"""
from functools import wraps


def route(bp, *args, **kwargs):
    """Route decorator for use in blueprints"""
    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator