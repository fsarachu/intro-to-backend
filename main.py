#!/usr/bin/env python

import webapp2

form = """
    <form method='post'>
        What is your birthday?
        <br><br>
        <label>Month: <input type='text' name='month' value='%(month)s'></label>
        <label>Day: <input type='text' name='day' value='%(day)s'></label>
        <label>Year: <input type='text' name='year' value='%(year)s'></label>
        <br><br>
        <div style='color: red'>%(error)s</div>
        <br>
        <input type='submit' value='Submit'>
    </form>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self, error='', month='', day='', year=''):
        self.response.write(form % {'error': error, 'month': month, 'day': day, 'year': year})

    def get(self):
        self.write_form()

    def post(self):
        from validators.MonthValidator import MonthValidator
        from validators.DayValidator import DayValidator
        from validators.YearValidator import YearValidator

        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        valid_month = MonthValidator.validate(self.request.get('month'))
        valid_day = DayValidator.validate(self.request.get('day'))
        valid_year = YearValidator.validate(self.request.get('year'))

        if not (valid_month and valid_day and valid_year):
            self.write_form(error='That doesn\'t look good buddy...', month=user_month, day=user_day, year=user_year)
        else:
            self.response.write('Thanks! That\'s a totally valid date!')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
