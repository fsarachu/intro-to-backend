import Handler


class ThanksHandler(Handler):
    def get(self):
        self.response.write('Thanks! That\'s a totally valid date!')
