from book import book, EBook
from library import Library

NIELIT_Library = Library()

book_1 = book("The jungle book", "Rudyard Kipling")
book_2 = book("Can be strangers again", "Shrijeet Shandilya")
ebook_1 = EBook("Python 101", "Guido van Rossum", "5MB")
book_1.borrow_book()
NIELIT_Library.add_books(book_1)
NIELIT_Library.add_books(book_2)
NIELIT_Library.add_books(ebook_1)
NIELIT_Library.show_available_books()
