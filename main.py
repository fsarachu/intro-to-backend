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


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
