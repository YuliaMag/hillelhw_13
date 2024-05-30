
class LibraryMember:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        book.borrow()

    def return_book(self, book):
        book.return_book()
