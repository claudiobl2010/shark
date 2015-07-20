# encoding: utf-8

from flask.views import MethodView
from flask import render_template

from shark import __version__, __release_date__


class HomeMethodView(MethodView):

    def get(self):

        return render_template('home.html', version=__version__, release_date=__release_date__)

