class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book {self.title} by {self.author} has been borrowed.")
        else:
            print("The book is not available yet.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book {self.title} by {self.author} has been returned.")
        else:
            print("This book is available.")


book1 = Book("'1984'", "George Orwell")
book2 = Book("'The Haunting of Hill House'", "Shirley Jackson")
book3 = Book("'Lord of the Flies'", "William Golding")
