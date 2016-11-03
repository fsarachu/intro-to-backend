import jinja2

import webapp2


class Handler(webapp2.RequestHandler):
    template_dir = '../templates'
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

    def write(self, *args, **kwargs):
        self.response.write(*args, **kwargs)

    def render_str(self, template, **kwargs):
        t = self.jinja_env.get_template(template)
        return t.render(kwargs)
