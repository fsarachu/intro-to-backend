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
        from validators.MonthValidator import MonthValidator
        from validators.DayValidator import DayValidator
        from validators.YearValidator import YearValidator

        user_month = MonthValidator.validate(self.request.get('month'))
        user_day = DayValidator.validate(self.request.get('day'))
        user_year = YearValidator.validate(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.response.write(form)
        else:
            self.response.write('Thanks! That\'s a totally valid date!')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
