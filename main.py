#!/usr/bin/env python

import webapp2


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
