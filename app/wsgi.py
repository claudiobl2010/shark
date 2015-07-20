# encoding: utf-8

import os
import sys


sys.path.insert(0, os.path.abspath('%s/../../' % os.path.abspath(os.path.dirname(__file__))))


from flask import Flask

from shark.app.routes import routes
from shark.app import config


app = Flask(__name__)

app.debug = True
app.template_folder = '%s/../templates' % app.root_path
app.static_folder = '%s/../static' % app.root_path
app.config.from_pyfile('config.py')

for url, view in routes:
    app.add_url_rule(url, view_func=view)

if __name__ == '__main__':
    app.run()

