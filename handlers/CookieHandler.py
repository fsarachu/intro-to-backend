import hashlib

from Handler import Handler


class CookieHandler(Handler):
    def get(self):
        # Cookies handling
        visits = self.request.cookies.get('visits', self.make_secure_value('0'))
        visits = self.check_secure_value(visits)
        
        if not visits:
            self.render('cookies.html', message='Ooooops! That cookie doesn\'t looks good')
            return 
        
        if visits.isdigit():
            visits = int(visits)
        else:
            visits = 0

        visits += 1

        self.response.headers.add_header('Set-Cookie', 'visits={}'.format(visits))

        if visits > 30:
            message = "You are AWESOME! You have visited this page {} times!".format(visits)
        else:
            message = "You are not cool enough... You have only visited this page {} times...".format(visits)

        self.render('cookies.html', message=message)

    def hash_str(self, s):
        return hashlib.md5(s).hexdigest()
    
    def make_secure_value(self, s):
        return '{},{}'.format(s,self.hash_str(s))

    def check_secure_value(self, s):
        value = (s.split(','))[0]
        return value if s == self.make_secure_value(value) else None
