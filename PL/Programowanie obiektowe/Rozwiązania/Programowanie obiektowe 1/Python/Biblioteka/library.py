## \brief Class representing a library.
class Library:
    ## \brief Initializes a Library object.
    def __init__(self):
        self.books = []
        self.members = []

    ## \brief Adds a member to the library.
    #  \param member The member to be added.
    def add_member(self, member):
        self.members.append(member)

    ## \brief Finds a book in the library by title.
    #  \param title The title of the book to find.
    #  \return The book object if found, otherwise None.
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    ## \brief Returns a string representation of the Library object.
    #  \return String representation of the Library object.
    def __str__(self):
        return f"Library has {len(self.books)} books and {len(self.members)} members."