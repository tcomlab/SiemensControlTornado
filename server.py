__author__ = 'Taras'


import sqlite3
import tornado
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.escape import json_encode
import threading
import time
import tornado.websocket

# MyModules

import main_page
import login_page
import arch_page
import alarm_page

# ----------------------------------------------------------------

class NotFound(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("404.html")
        pass

# Server configuration Def
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", main_page.HomeHandler),
            (r"/login", login_page.LoginHandler),
            (r"/arch", arch_page.ArchHandler),
            (r"/alarm", alarm_page.AlarmHandler),
            #(r"/rest", ResrHandler),
            #(r"/archive", ArchiveHandler),
            #(r"/feed", FeedHandler),
            #(r"/entry/([^/]+)", EntryHandler),
            #(r"/compose", ComposeHandler),
            #(r"/auth/login", AuthLoginHandler),
            #(r"/auth/logout", AuthLogoutHandler),
            #(r'/(*)', NotFound),
        ]
        settings = dict(
            blog_title=u"Tornado Blog",
            template_path="www",
            static_path="static",
            #ui_modules={"Entry": EntryModule},
            xsrf_cookies=True,
            cookie_secret="8$cFH| 1O:-ZDTBnh--#(z/Kp?gl4F1NfFYqvCi|Lb+D>=*c*zpsuaUKvt|XI`wS",
            #login_url="/auth/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
        self.db = sqlite3.connect("dneprobase.sqlite")

def main():

    #my_thread = MyThread()
    #my_thread.name = 0
    #my_thread.start()



    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()