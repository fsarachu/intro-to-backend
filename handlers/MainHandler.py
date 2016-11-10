from Handler import Handler


class MainHandler(Handler):
    def get(self):
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

        self.render('index.html', message=message)
