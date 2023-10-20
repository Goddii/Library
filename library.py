class Book:
    def __init__(self, title, genre, author, number_books,book_id ,availability_status=True):
        self.title = title
        self.genre = genre
        self.author = author
        self.book_id = book_id
        self.availability_status = availability_status

    def __str__(self):
        return f'Book ID: {self.book_id} \nTitle: {self.title} \nGenre: {self.genre} \nAuthor: {self.author} \nAvailability: {"Available" if self.availability_status  else "Unavailable"} '


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input('Enter title of book: ')
        genre = input('Enter genre of the book: ')
        author = input('Enter author of book: ')
        book_id = len(self.books) + 1
        book = Book(title, genre, author, book_id)
        self.books.append(book)
        print(f'You have added the book with title {book.title} to the library')

    def search_book(self):
        search_title = input('Enter title of book to search: ')
        found_book = []
        for book in self.books:
            if book.title.lower() == search_title.lower():
                found_book.append(book)
        if found_book:
            print(f'Found {len(found_book)} books with the title {search_title} in the library')
            print('<-------------------------------------------------------------->')
            for book in found_book:
                print(book)
                print('|------------------------------------------------------------|')
        else:
            print(f'No book with the title {search_title} is in the library')

    def display_all_books(self):
        print('--HERE ARE THE AVAILABLE BOOKS--')
        if self.books:
            for book in self.books:
                print(book)
                print('-------------------------------------------')
        else:
            print(f'No book available in library')

    def borrow_book(self):
        search_title = input('Enter book to borrow: ')
        for book in self.books:
            if book.title.lower() == search_title.lower():
                if book.availability_status:
                    book.availability_status = False
                    print(f'Book with title {book.title} successfully borrowed from Library')
                else:
                    print(f'Book with title {book.title} is unavailable to borrow')
                return
        print(f'No book with title {search_title} is in library')

    def return_book(self):
        search_title = input('Enter title of book to return: ')
        for book in self.books:
            if book.title.lower() == search_title.lower():
                if not book.availability_status:
                    book.availability_status = True
                    print(f'Book with title {book.title} successfully returned to Library')
                else:
                    print(f'Book with title {book.title} already available in Library')
                return
        print(f'Book with that title {search_title} is not in Library')

    def delete_book(self):
        search_title = input('Enter title of book you want to delete: ')
        for book in self.books:
            if book.title.lower() == search_title.lower():
                self.books.remove(book)
                print(f'Book with title {book.title} removed successfully')
                return
        print(f'Book with title {search_title} is no longer in library')

def display_menu():
    print('LIBRARY MANAGEMENT SYSTEM')
    print('1. ADD BOOK')
    print('2. SEARCH BOOK')
    print('3. DISPLAY BOOK')
    print('4. BORROW BOOK')
    print('5. RETURN BOOK')
    print('6. REMOVE BOOK')
    print('7. QUIT')

def main():
    library = Library()
    display_menu()
    while True:
        choice = input('Enter a choice between 1-7: ')
        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.search_book()
        elif choice == '3':
            library.display_all_books()
        elif choice == '4':
            library.borrow_book()
        elif choice == '5':
            library.return_book()
        elif choice == '6':
            library.delete_book()
        elif choice == '7':
            print('Thank you for using LMS')
            break
        else:
            print('Invalid choice.Please try again')

if __name__ == '__main__':
    main()
