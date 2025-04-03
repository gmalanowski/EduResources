## \brief Class representing a member.
class Member:
    ## \brief Initializes a Member object.
    #  \param name The name of the member.
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    ## \brief Borrows a book for the member.
    #  \param book The book to be borrowed.
    #  \return True if the book was successfully borrowed, otherwise False.
    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return True
        return False

    ## \brief Returns a borrowed book.
    #  \param book The book to be returned.
    #  \return True if the book was successfully returned, otherwise False.
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return True
        return False

    ## \brief Returns a string representation of the Member object.
    #  \return String representation of the Member object.
    def __str__(self):
        return f"Member: {self.name}, Borrowed books: {[book.title for book in self.borrowed_books]}"