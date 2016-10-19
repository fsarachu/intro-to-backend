#!/usr/bin/env python

import webapp2

form = """
    <form method='post' action='/testform'>
        <input type='search' name='q'>
        <input type='submit'>
    </form>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)


class TestHandler(webapp2.RequestHandler):
    def get(self):
        q = self.request.get("q")
        self.response.write("GET: " + q)

    def post(self):
        q = self.request.get("q")
        self.response.write("POST: " + q)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)
], debug=True)
