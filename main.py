#!/usr/bin/env python

import webapp2

form = """
    <form>
        <label><input type='radio' name='q' value='one'>One</label>
        <label><input type='radio' name='q' value='two'>Two</label>
        <label><input type='radio' name='q' value='three'>Three</label>
        <br>
        <input type='submit'>
    </form>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)


class TestHandler(webapp2.RequestHandler):
    def get(self):
        q = self.request.get("q")
        self.response.write(q)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)
], debug=True)
