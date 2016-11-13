import hashlib

from Handler import Handler


class CookieHandler(Handler):
    def get(self):
        user_cookie_str = self.request.cookies.get('visits', self.make_secure_value('0'))
        user_cookie_val = self.check_secure_value(user_cookie_str)
        
        if user_cookie_val and user_cookie_val.isdigit():
            visits = int(user_cookie_val)
            visits += 1
            new_cookie_str = self.make_secure_value(str(visits))
            self.response.headers.add_header('Set-Cookie', 'visits={}'.format(new_cookie_str))
            self.render('cookies.html', message='You have visited this page {} times'.format(visits))
        else:
            self.render('cookies.html', message='Ooooops! That cookie doesn\'t look good...')
        
    def hash_str(self, s):
        return hashlib.md5(s).hexdigest()
    
    def make_secure_value(self, s):
        return '{}-{}'.format(s,self.hash_str(s))

    def check_secure_value(self, s):
        value = s.split('-')[0]
        return value if s == self.make_secure_value(value) else None
