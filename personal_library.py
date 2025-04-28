import json

class BookCollection:
    """Manage your personal collection of books easily."""

    def __init__(self):
        """Initialize the book collection and load any previously saved data."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.load_books_from_storage()

    def load_books_from_storage(self):
        """Load books from a JSON file if available."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def persist_books_to_storage(self):
        """Save the current collection to a JSON file."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def add_new_book_entry(self):
        """Create a new book record from user input."""
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.persist_books_to_storage()
        print("Book added successfully!\n")

    def remove_book_entry(self):
        """Delete a book based on the title provided by the user."""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.persist_books_to_storage()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")

    def search_book_records(self):
        """Find books by title or author."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No matching books found.\n")

    def modify_book_details(self):
        """Update details of an existing book."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"
                )
                self.persist_books_to_storage()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")

    def display_all_books(self):
        """Show all books in the collection."""
        if not self.book_list:
            print("Your collection is empty.\n")
            return

        print("Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print()

    def display_reading_statistics(self):
        """Show progress of books read vs total books."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def launch_book_manager(self):
        """Launch the interactive book manager menu."""
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.add_new_book_entry()
            elif user_choice == "2":
                self.remove_book_entry()
            elif user_choice == "3":
                self.search_book_records()
            elif user_choice == "4":
                self.modify_book_details()
            elif user_choice == "5":
                self.display_all_books()
            elif user_choice == "6":
                self.display_reading_statistics()
            elif user_choice == "7":
                self.persist_books_to_storage()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.launch_book_manager()  