from Handler import Handler


class TemplateHandler(Handler):
    def get(self):
        items = [item.capitalize() for item in self.request.get_all('food')]

        self.render('shopping_list.html', items=items)
