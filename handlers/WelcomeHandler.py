from handlers.Handler import Handler
from validators import SignupValidator

class WelcomeHandler(Handler):
    validator = SignupValidator.SignupValidator()

    def get(self):
        username = self.request.get('username')

        if not self.validator.valid_username(username):
            self.render('welcome.html', username=username)
        else:
            self.redirect('signup.html')


