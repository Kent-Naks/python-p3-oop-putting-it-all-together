class Book:
    def __init__(self, title, page_count, author=None):
        self.title = title
        self.author = author
        self.page_count = page_count

    def read_book(self):
        print(f"Reading {self.title} by {self.author}.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        elif value > 0:
            self._page_count = value
        else:
            raise ValueError("Page count must be greater than zero.")

    # Adding the turn_page method
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
