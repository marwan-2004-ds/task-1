from Member import Member
from Book import Book
from StaffMember import StaffMember
from Library import Library

library = Library()


staff = StaffMember("Omar", "mm1234", "STF123")
book1 = Book("Learn Python", "Dr. Adam ", "123456789")
book2 = Book("AI for Beginners", "Reem ", "987654321")
staff.add_book(library, book1)
staff.add_book(library, book2)


library.show_books()


member = Member("Lina", "MEM002")
member.borrow_book(book1)
library.show_books()


member.return_book(book1)
library.show_books()
