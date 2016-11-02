#!/usr/bin/env python

import webapp2

form = """
    <form method='post'>
        What is your birthday?
        <br><br>
        <label>Month: <input type='text' name='month'></label>
        <label>Day: <input type='text' name='day'></label>
        <label>Year: <input type='text' name='year'></label>
        <br><br>
        <input type='submit' value='Submit'>
    </form>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        from validators import DayValidator
        if DayValidator.DayValidator.validate(self.request.get('day')):
            self.response.write("Thanks! Thats a totally valid day!")
        else:
            self.response.write("Oooops! check that day!")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
