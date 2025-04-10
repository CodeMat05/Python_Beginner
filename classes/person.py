class Person:
    def __init__(self, first_name, last_name, middle_initial):
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
    def get_fullName(self):
        return f'{self._last_name} {self._middle_initial} {self._first_name}'

    _first_name = ''
    _middle_initial = ''
    _last_name = ''
    _gender = 'female'