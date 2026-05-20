class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        try:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            for book in self.books:
                if book.book_id == book_id:
                    print("Book ID already exists.")
                    return

            new_book = Book(book_id, title, author)
            self.books.append(new_book)
            print("Book added successfully.")

        except ValueError:
            print("Invalid input. Book ID must be a number.")

    def view_books(self):
        if not self.books:
            print("No books available in library.")
            return

        print("\n----- BOOK LIST -----")
        for book in self.books:
            print(book)

    def search_book(self):
        title = input("Enter book title to search: ").lower()

        found = False
        for book in self.books:
            if title in book.title.lower():
                print(book)
                found = True

        if not found:
            print("Book not found.")

    def issue_book(self):
        try:
            book_id = int(input("Enter Book ID to issue: "))

            for book in self.books:
                if book.book_id == book_id:
                    if book.is_issued:
                        print("Book is already issued.")
                    else:
                        book.is_issued = True
                        print("Book issued successfully.")
                    return

            print("Book ID not found.")

        except ValueError:
            print("Invalid Book ID.")

    def return_book(self):
        try:
            book_id = int(input("Enter Book ID to return: "))

            for book in self.books:
                if book.book_id == book_id:
                    if not book.is_issued:
                        print("Book was not issued.")
                    else:
                        book.is_issued = False
                        print("Book returned successfully.")
                    return

            print("Book ID not found.")

        except ValueError:
            print("Invalid Book ID.")

    def remove_book(self):
        try:
            book_id = int(input("Enter Book ID to remove: "))

            for book in self.books:
                if book.book_id == book_id:
                    self.books.remove(book)
                    print("Book removed successfully.")
                    return

            print("Book ID not found.")

        except ValueError:
            print("Invalid Book ID.")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Remove Book")
    print("7. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.remove_book()

    elif choice == "7":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
