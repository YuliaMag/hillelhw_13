import Library
import Book
import LibraryMember

# Create some books
b1 = Book.book1
b2 = Book.book2
b3 = Book.book3

# Create a library
library = Library.Library()

# Add books to the library
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

# Create a library member
member = LibraryMember.LibraryMember("John Doe")

# Display available books in the library
library.display_books()

# John borrows a book
member.borrow_book(b1)

# Try to borrow the same book again
member.borrow_book(b1)

# Display available books after John returns the book
library.display_books()

# John returns the book
member.return_book(b1)

# Display available books after John returns the book
library.display_books()
