Python

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def _find_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        book = self._find_book(title)
        if book and book.is_available():
            book.check_out()
            print(f"'{title}' has been checked out.")
        elif book:
            print(f"'{title}' is already checked out.")
        else:
            print(f"'{title}' not found in the library.")

    def return_book(self, title):
        book = self._find_book(title)
        if book and not book.is_available():
            book.return_book()
            print(f"'{title}' has been returned.")
        elif book:
            print(f"'{title}' was not checked out.")
        else:
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)