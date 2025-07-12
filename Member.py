
class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def get_membership_id(self):
            return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id
