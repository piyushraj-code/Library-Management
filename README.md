# Library-Management
# 📚 Smart Library Management System

A Python-based console application that simulates a real-world library system. This project demonstrates core **Object-Oriented Programming (OOP)** concepts including Classes, Objects, Inheritance, Composition, and Polymorphism.

## 🚀 Features

* **Book Management:** Add different types of books to the library catalog.
* **Smart Borrowing System:** Users can borrow books only if they are available.
* **Automatic Status Updates:** The system automatically tracks availability (True/False) when books are borrowed or returned.
* **E-Book Support:** Specialized handling for Digital Books (E-Books) including file size tracking.
* **Polymorphic Display:** The system intelligently displays information based on whether the item is a physical Book or an E-Book.

## 🛠️ Concepts Applied

* **Encapsulation:** Data (like `title`, `author`, `is_available`) is bundled safely within objects.
* **Inheritance:** `EBook` class inherits attributes from the parent `Book` class.
* **Composition:** The `Library` class manages a collection (list) of `Book` objects.
* **Polymorphism:** The `display_info()` method behaves differently for standard Books vs. E-Books.

## 📂 Project Structure

This project uses a modular design with three separate files:

1.  **`book.py`**
    * Contains the `Book` class (Blueprint for physical books).
    * Contains the `EBook` class (Inherits from Book, adds `file_size`).
2.  **`library.py`**
    * Contains the `Library` class (Manages the list of books).
    * Handles adding books and displaying available ones.
3.  **`main.py`**
    * The entry point of the program.
    * Creates objects, simulates borrowing/returning, and runs the system.

## 💻 How to Run

1.  Ensure you have Python installed.
2.  Save the files (`book.py`, `library.py`, `main.py`) in the same folder.
3.  Run the main script:

```bash
python main.py

# 📋 Example Usage
# Creating books
book1 = Book("The Jungle Book", "Rudyard Kipling")
ebook1 = EBook("Python 101", "Guido van Rossum", "5MB")

# Borrowing logic
book1.borrow_book()  # Output: You have borrowed The Jungle Book

# Library Display
library.show_available_books()
# Output:
# Title: Python 101 | Author: Guido van Rossum | File_Size: 5MB

# 🔮 Future Improvements
Add a User class to track who borrowed the book.

Implement a fine calculation system for late returns.

Add a database (SQL) to save book records permanently.


