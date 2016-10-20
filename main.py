#!/usr/bin/env python

import webapp2

form = """
    <form>
        <select name='q'>
            <option value='one'>Kangaroo</option>
            <option value='two'>Parrot</option>
            <option value='three'>Cheetah</option>
        </select>
        <br><br>
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
