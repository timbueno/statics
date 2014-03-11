# -*- coding: utf-8 -*-
"""
    app
    ~~~~~~~~~~~~~~

    statics app module
"""
import os
import sys

from statics.core import create_app
from statics.extensions import freezer
from statics.settings import DevConfig, ProdConfig


## FIX ME
# print os.environ.get("STATICS_ENV")

if os.environ.get("STATICS_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run()
