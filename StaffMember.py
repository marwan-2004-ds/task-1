from Member import Member


class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Staff {self.name} added the book '{book.title}' to the library.")
