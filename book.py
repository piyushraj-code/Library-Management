class book:
    def __init__(self, title, author, is_available = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def display_info(self):
        print(f"Title: {self.title} | Author: {self.author} | Available: {self.is_available}")

    def borrow_book(self):
        if(self.is_available):
            print(f"You have borrowed {self.title}")
            self.is_available = False
        else:
            print(f"Soryy {self.title} is not currently available")

    def return_book(self):
        print(f"{self.title} has been returned")
        self.is_available = True

class EBook(book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display_info(self):
        print(f"Title: {self.title} | Author: {self.author} | File_Size: {self.file_size}")