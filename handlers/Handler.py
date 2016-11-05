import jinja2
import os

import webapp2


class Handler(webapp2.RequestHandler):
    template_dir = os.path.join(os.path.dirname(__file__), '../templates')
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

    def write(self, *args, **kwargs):
        self.response.write(*args, **kwargs)

    def render_str(self, template, **kwargs):
        t = self.jinja_env.get_template(template)
        return t.render(kwargs)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))
