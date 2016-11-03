#!/usr/bin/env python

import webapp2


class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.write(*args, **kwargs)


class MainHandler(Handler):
    main_page = """
        <!doctype html>
        <html lang='en'>
        <head>
          <meta charset='UTF-8'>
          <meta name='viewport' content='width=device-width, initial-scale=1.0'>
          <meta http-equiv='X-UA-Compatible' content='ie=edge'>
          <title>Intro to Backend</title>
        </head>
        <body>
          <h1>Intro to Backend</h1>
          <ul>
            <li><a href='/form'>Forms</a></li>
            <li><a href='/template'>Templates</a></li>
          </ul>
        </body>
        </html>
        """

    def get(self):
        self.response.write(self.main_page)


class FormHandler(Handler):
    form = """
        <form method='post'>
            What is your birthday?
            <br><br>
            <label>Month: <input type='text' name='month' value='%(month)s'></label>
            <label>Day: <input type='number' name='day' value='%(day)s'></label>
            <label>Year: <input type='number' name='year' value='%(year)s'></label>
            <br><br>
            <div style='color: red'>%(error)s</div>
            <br>
            <input type='submit' value='Submit'>
        </form>
    """

    @staticmethod
    def html_escape(s):
        import cgi
        return cgi.escape(s, quote=True)

    def write_form(self, error='', month='', day='', year=''):
        self.response.write(self.form % {
            'error': self.html_escape(error),
            'month': self.html_escape(month),
            'day': self.html_escape(day),
            'year': self.html_escape(year)
        })

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
            self.write_form(error='That doesn\'t look good buddy...', month=user_month, day=user_day,
                            year=user_year)
        else:
            self.redirect('/form/thanks')


class ThanksHandler(Handler):
    def get(self):
        self.response.write('Thanks! That\'s a totally valid date!')


class TemplateHandler(Handler):
    pass


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/form', FormHandler),
    ('/form/thanks', ThanksHandler),
    ('/template', TemplateHandler)
], debug=True)
