## \brief Class representing a book.
class Book:
    ## \brief Initializes a Book object.
    #  \param title The title of the book.
    #  \param author The author of the book.
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    ## \brief Returns a string representation of the Book object.
    #  \return String representation of the Book object.
    def __str__(self):
        return f"{self.title} by {self.author} - {'Available' if self.is_available else 'Checked out'}"