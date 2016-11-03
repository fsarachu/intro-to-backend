#!/usr/bin/env python

import webapp2


class TemplateHandler(Handler):
    pass


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/form', FormHandler),
    ('/form/thanks', ThanksHandler),
    ('/template', TemplateHandler)
], debug=True)
