from Handler import Handler


class TemplateHandler(Handler):
    form_html = """
    <form action=''>
        <h2>Add Food</h2>
        <input type='text' name='food' autofocus='autofocus'>
        <input type='submit' value='Add'>
    </form>
    """

    def get(self):
        self.write(self.form_html)
