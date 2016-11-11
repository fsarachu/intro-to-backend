import hashlib

from handlers import Handler


class CookieHandler(Handler):
    def get(self):
        # Cookies handling
        visits = self.request.cookies.get('visits', '0')
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

        # Hashing stuff
        hashed = []

        x = 'Hello World!'
        hashed_item = dict(x=x, y=hashlib.md5(x).hexdigest(), algorithm='md5')
        hashed.append(hashed_item)

        x = 'Hello world!'
        hashed_item = dict(x=x, y=hashlib.md5(x).hexdigest(), algorithm='md5')
        hashed.append(hashed_item)

        x = 'Hello World!'
        hashed_item = dict(x=x, y=hashlib.sha1(x).hexdigest(), algorithm='sha1')
        hashed.append(hashed_item)

        x = 'Hello World!'
        hashed_item = dict(x=x, y=hashlib.sha256(x).hexdigest(), algorithm='sha256')
        hashed.append(hashed_item)

        self.render('cookies.html', message=message, hashed=hashed)
