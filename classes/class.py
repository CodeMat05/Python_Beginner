from person import Person
from user_account import UserAccount


class StudentUser(Person):
    course = ''
    
    def display_name(self):
        return self._first_name

s = StudentUser('Luffy', 'Monkey', 'D')
print(s.get_fullName())
print(s.display_name())

