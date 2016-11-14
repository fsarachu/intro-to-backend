import hashlib
import hmac
import random
import string

from Handler import Handler


class CookieHandler(Handler):
    SALT = 'somesalt'

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
        return hmac.new(self.SALT, s).hexdigest()

    def make_secure_value(self, s):
        return '{}-{}'.format(s, self.hash_str(s))

    def check_secure_value(self, s):
        value = s.split('-')[0]
        return value if s == self.make_secure_value(value) else None

    @staticmethod
    def make_salt(length=5):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def make_password_hash(self, name, password):
        salt = self.make_salt()
        h = hashlib.sha256(name + password + salt).hexigest()
        return '{},{}'.format(h, salt)


if __name__ == '__main__':
    for i in range(50):
        print CookieHandler.make_salt(20)
