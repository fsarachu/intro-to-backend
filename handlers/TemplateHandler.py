from Handler import Handler


class TemplateHandler(Handler):
    form_html = """
    <form action=''>
        <h2>Add Food</h2>
        <input type='text' name='food' autofocus='autofocus'>
        %s
        <input type='submit' value='Add'>
    </form>
    """

    hidden_html = """
    <input type='hidden' name='food' value='%s'>
    """

    shopping_list_html = """
    <br><br>
    <h2>Shopping List</h2>
    <ul>
    %s
    </ul>
    """

    def get(self):
        self.write(self.form_html)
