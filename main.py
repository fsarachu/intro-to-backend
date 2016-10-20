#!/usr/bin/env python

import webapp2

loginform = """
    <form method='post' action='/testform'>
        <label>Nickname: <input type='text' name='nickname'></label>
        <label>Password: <input type='password' name='password'></label>
        <input type='submit'>
    </form>
"""

form = """
    <form action='/testform'>
        <input type='checkbox' name='q'>
        <input type='checkbox' name='r'>
        <input type='checkbox' name='s'>
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

    def post(self):
        nickname = self.request.get("nickname")
        password = self.request.get("password")

        if nickname == "franco" and password == "secret":
            self.response.write("Logged In!")
        else:
            self.response.write("Wrong username or password! Try again...")
            self.response.write(loginform)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)
], debug=True)
