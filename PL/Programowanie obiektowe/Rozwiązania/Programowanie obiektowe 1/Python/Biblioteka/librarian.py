## \brief Class representing a librarian.
class Librarian:
    ## \brief Initializes a Librarian object.
    #  \param name The name of the librarian.
    def __init__(self, name):
        self.name = name

    ## \brief Adds a book to the library.
    #  \param library The library to which the book will be added.
    #  \param book The book to be added.
    def add_book(self, library, book):
        library.books.append(book)

    ## \brief Returns a string representation of the Librarian object.
    #  \return String representation of the Librarian object.
    def __str__(self):
        return f"Librarian: {self.name}"