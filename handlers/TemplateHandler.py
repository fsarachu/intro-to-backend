from Handler import Handler


class TemplateHandler(Handler):
    # hidden_html = """
    # <input type='hidden' name='food' value='%s'>
    # """
    #
    # item_html = """
    # <li>%s</li>
    # """
    #
    # shopping_list_html = """
    # <h2>Shopping List</h2>
    # <ul>
    # %s
    # </ul>
    # """
    #
    def get(self):
        n = (self.request.get('n'))

        if n.isdigit():
            n = int(n)

        self.render('shopping_list.html', n=n)
        #     output = self.form_html
        #     output_hidden = ""
        #     output_items = ""
        #
        #     items = self.request.get_all('food')
        #
        #     if items:
        #         for item in items:
        #             output_hidden += self.hidden_html % item
        #             output_items += self.item_html % item.capitalize()
        #
        #         output_shopping = self.shopping_list_html % output_items
        #
        #         output += output_shopping
        #
        #     output = output % output_hidden
        #
        #     self.write(output)
