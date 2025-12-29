from book import book, EBook
class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def show_available_books(self):
        for book in self.books:
            if (book.is_available):
                book.display_info()