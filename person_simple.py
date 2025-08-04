
from datetime import date

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def get_age(self):
        current_year = date.today().year
        return current_year - self.birth_year

# تجربة الكلاس
p1 = Person("Ali", "Egypt", 2000)
print("Name:", p1.name)
print("Country:", p1.country)
print("Age:", p1.get_age())
