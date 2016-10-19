#!/usr/bin/env python

import webapp2

form = """
    <form action='/testform'>
        <input type='search' name='q'>
        <input type='submit'>
    </form>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)


class TestHandler(webapp2.RequestHandler):
    def get(self):
        # q = self.request.get("q")
        # self.response.write(q)
        self.response.headers['Content-Type'] = "text/plain"
        self.response.write(self.request)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)
], debug=True)
