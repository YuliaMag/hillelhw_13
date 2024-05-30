class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if self.books:
            print("Available Books:")
            for book in self.books:
                if not book.is_borrowed:
                    print(f"- {book.title} by {book.author}")
        else:
            print("No books available in the library.")
