class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_issued = False  # Encapsulated attribute

    def issue(self):
        if not self.__is_issued:
            self.__is_issued = True
            return True
        return False

    def return_book(self):
        self.__is_issued = False

    def __str__(self):
        status = 'Issued' if self.__is_issued else 'Available'
        return f"{self.title} by {self.author} - {status}"


class Ebook(Book):
    def __init__(self, title, author, filesize):
        super().__init__(title, author)
        self.file_size = filesize

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, File Size: {self.file_size} MB"


def main():
    books = {}
    book_id = 1

    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Add Ebook")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                books[book_id] = Book(title, author)
                print(f"Book added with ID {book_id}")
                book_id += 1

            case 2:
                title = input("Enter ebook title: ")
                author = input("Enter ebook author: ")
                size = float(input("Enter file size in MB: "))
                books[book_id] = Ebook(title, author, size)
                print(f"Ebook added with ID {book_id}")
                book_id += 1

            case 3:
                bid = int(input("Enter book ID to issue: "))
                if bid in books:
                    if books[bid].issue():
                        print("Book issued successfully.")
                    else:
                        print("Book is already issued.")
                else:
                    print("Book ID not found.")

            case 4:
                bid = int(input("Enter book ID to return: "))
                if bid in books:
                    books[bid].return_book()
                    print("Book returned successfully.")
                else:
                    print("Book ID not found.")

            case 5:
                print("\n--- Book List ---")
                for bid, book in books.items():
                    print(f"ID {bid}: {book}")

            case 6:
                print("Exiting... Goodbye!")
                break

            case _:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
