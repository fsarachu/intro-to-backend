#!/usr/bin/env python

import webapp2
from handlers import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/form', FormHandler),
    ('/form/thanks', ThanksHandler),
    ('/template', TemplateHandler)
], debug=True)
