from Handler import Handler


class MainHandler(Handler):
    main_page = """
        <!doctype html>
        <html lang='en'>
        <head>
          <meta charset='UTF-8'>
          <meta name='viewport' content='width=device-width, initial-scale=1.0'>
          <meta http-equiv='X-UA-Compatible' content='ie=edge'>
          <title>Intro to Backend</title>
        </head>
        <body>
          <h1>Intro to Backend</h1>
          <ul>
            <li><a href='/form'>Forms</a></li>
            <li><a href='/template'>Templates</a></li>
          </ul>
        </body>
        </html>
        """

    def get(self):
        self.write(self.main_page)
