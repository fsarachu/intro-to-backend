from Handler import Handler


class SignupHandler(Handler):
    def get(self):
        self.render('signup.html')

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username=username, email=email)

        if have_error == True:
            self.render('signup.html', **params)
        else:
            self.redirect('/welcome?username={}'.format(username))
