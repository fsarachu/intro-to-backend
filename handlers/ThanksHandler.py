from Handler import Handler


class ThanksHandler(Handler):
    def get(self):
        self.write('Thanks! That\'s a totally valid date!')
