# encoding: utf-8

from shark.views.home import HomeMethodView


routes = []

routes.append(('/', HomeMethodView.as_view('home')))
