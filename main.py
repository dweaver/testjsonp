#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tornado app for testing jsonp from localhost

import os.path
import os
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import json
import urllib2
from pprint import pprint


# import and define tornado-y things
from tornado.options import define, options
define("port", default=5000, help="run on the given port", type=int)

# Google analytics ID for this site
ANALYTICSID = False  # "UA-34045230-1"

# application settings and handle mapping info
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/test", Handler),
        ]
        settings = dict(
            template_path =
                os.path.join(os.path.dirname(__file__), "templates"),
            static_path =
                os.path.join(os.path.dirname(__file__), "templates/static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class Handler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write('[{"title": "Temperature"}, {"title": "Humidity"}]')
        self.finish()
 

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(os.environ.get("PORT", 5000))

    # start it up
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
