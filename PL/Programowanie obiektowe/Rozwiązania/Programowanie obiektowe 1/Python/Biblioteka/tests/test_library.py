from book import Book
from librarian import Librarian
from library import Library
from member import Member
from utils.file_operations import load_books, save_books, load_members, save_members, load_history, save_history

## \brief Creates a list of Book objects from data.
#  \param books_data List of dictionaries containing book data.
#  \return List of Book objects.
def create_books_from_data(books_data):
    books = []
    for book_data in books_data:
        book = Book(book_data['title'], book_data['author'])
        book.is_available = book_data['is_available']
        books.append(book)
    return books

## \brief Creates a list of Member objects from data.
#  \param members_data List of dictionaries containing member data.
#  \return List of Member objects.
def create_members_from_data(members_data):
    members = []
    for member_data in members_data:
        member = Member(member_data['name'])
        for book_data in member_data['borrowed_books']:
            book = Book(book_data['title'], book_data['author'])
            book.is_available = book_data['is_available']
            member.borrowed_books.append(book)
        members.append(member)
    return members

## \brief Main function for managing the library.
def main():
    books_data = load_books('data/books_data.json')
    members_data = load_members('data/members_data.json')
    history = load_history('data/history.txt')

    library = Library()
    librarian = Librarian("John")
    library.books = create_books_from_data(books_data)
    library.members = create_members_from_data(members_data)

    while True:
        print("\n1. Add book")
        print("2. Add member")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Display library status")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            librarian.add_book(library, book)
            save_books('data/books_data.json', [{'title': b.title, 'author': b.author, 'is_available': b.is_available} for b in library.books])
            print(f"Added book: {book}")

        elif choice == '2':
            name = input("Enter member name: ")
            member = Member(name)
            library.add_member(member)
            save_members('data/members_data.json', [{'name': m.name, 'borrowed_books': [{'title': b.title, 'author': b.author, 'is_available': b.is_available} for b in m.borrowed_books]} for m in library.members])
            print(f"Added member: {member}")

        elif choice == '3':
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            member = next((m for m in library.members if m.name == member_name), None)
            book = library.find_book(book_title)
            if member and book:
                if member.borrow_book(book):
                    save_history('data/history.txt', [f"{member.name} borrowed {book.title}"])
                    save_books('data/books_data.json', [{'title': b.title, 'author': b.author, 'is_available': b.is_available} for b in library.books])
                    print(f"{member.name} borrowed the book: {book.title}")
                else:
                    print("The book is not available.")
            else:
                print("Member or book not found.")

        elif choice == '4':
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            member = next((m for m in library.members if m.name == member_name), None)
            book = library.find_book(book_title)
            if member and book:
                if member.return_book(book):
                    save_history('data/history.txt', [f"{member.name} returned {book.title}"])
                    save_books('data/books_data.json', [{'title': b.title, 'author': b.author, 'is_available': b.is_available} for b in library.books])
                    print(f"{member.name} returned the book: {book.title}")
                else:
                    print("The member did not borrow this book.")
            else:
                print("Member or book not found.")

        elif choice == '5':
            print(library)
            for member in library.members:
                print(member)
            for book in library.books:
                print(book)

        elif choice == '6':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()