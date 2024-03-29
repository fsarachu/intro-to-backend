from Handler import Handler
from validators import SignupValidator


class SignupHandler(Handler):
    validator = SignupValidator.SignupValidator()

    def get(self):
        self.render('signup.html')

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username=username, email=email)

        if not self.validator.valid_username(username):
            params['error_username'] = 'Username is not valid!'
            have_error = True

        if not self.validator.valid_password(password):
            params['error_password'] = 'Password is not valid!'
            have_error = True
        elif password != verify:
            params['error_verify'] = 'Passwords do not match!'
            have_error = True

        if not self.validator.valid_email(email):
            params['error_email'] = 'Email is not valid!'
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            self.redirect('/welcome?username={}'.format(username))
