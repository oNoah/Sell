#!/usr/bin/env python3
#coding: utf-8

__author__ = 'CrazySheep'


import tornado.ioloop
import tornado.web
import os
from tornado.web import StaticFileHandler
# import tornado.options

# from tornado.options import define, options
# define("port", default=8000, help="run on the given port", type=int)

# class BaseHandler(tornado.web.RequestHandler):
#      def get_current_user(self):
#         user_id = self.get_secure_cookie("user")
#         if not user_id: return None
#         return self.backend.get_user_by_id(user_id)

#     def get_user_locale(self):
#         if "locale" not in self.current_user.prefs:
#             Use the Accept-Language header
#             return None
#         return self.current_user.prefs["locale"]

class BaseHandler(tornado.web.RequestHandler):
    def get_user_locale(self):
        user_locale = self.get_argument('lang', None)
        print(user_locale)
        if user_locale == 'en':
            return tornado.locale.get('en_US')
        elif user_locale == 'tw':
            return tornado.locale.get('zh_CN')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        _ = self.locale.translate

        self.render("templates/index.html")

class CategoriesHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/categories.html")



TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")  # 这里增加设置了静态路径

CSS_URL = os.path.join(os.path.dirname(__file__), "static/css")
JS_URL = os.path.join(os.path.dirname(__file__), "static/js")
IMG_URL = os.path.join(os.path.dirname(__file__), "static/img")
IMAGES_URL = os.path.join(os.path.dirname(__file__), "static/images")
FONTS_URL = os.path.join(os.path.dirname(__file__), "static/fonts")

i18n_path = os.path.join(os.path.dirname(__file__), "locales")

handlers = [(r"/", MainHandler),
            (r"/index", MainHandler),
            (r"/categories", CategoriesHandler),
            (r"/static/(.*)", StaticFileHandler,{"path": STATIC_PATH}),
            (r"/template/(.*)", StaticFileHandler, {"path": TEMPLATE_PATH}),
            (r"/locales/(.*)", StaticFileHandler, {"path": i18n_path}),
            (r"/css/(.*)", StaticFileHandler, {"path": CSS_URL}),
            (r"/js/(.*)", StaticFileHandler, {"path": JS_URL}),
            (r"/img/(.*)", StaticFileHandler, {"path": IMG_URL}),
            (r"/images/(.*)", StaticFileHandler, {"path": IMAGES_URL}),
            (r"/fonts/(.*)", StaticFileHandler, {"path": FONTS_URL}),
             (r"/(.html)", StaticFileHandler, {"path": TEMPLATE_PATH}),
            ]

app = tornado.web.Application(handlers)

if __name__ == "__main__":
    tornado.locale.load_translations(i18n_path)
    tornado.locale.set_default_locale("zh_CN")

    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
