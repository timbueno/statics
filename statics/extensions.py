# -*- coding: utf-8 -*-
"""
    statics.extensions
    ~~~~~~~~~~~~~~

    Extensions module. Each extension is initialized in the app factory located
    in core.py
"""

from flask.ext.flatpages import FlatPages
flatpages = FlatPages()

from flask.ext.frozen import Freezer
freezer = Freezer()