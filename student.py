"""
Real World Test
Test Driven Development with the student class
"""
from datetime import date, timedelta


class Student:
    """
    A student class as base for method testing
    """
    def __init__(self, first_name, last_name):
        """
        As we want these to be read-only fields, we can prepend the first_name
        and last_name properties with an underscore so other developers know
        how it should be used.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        """
        This is a read-only method to get more detailed information about a
         student, such as the student’s full name.
        Has self as a parameter and return an f-string consisting of
         self._first_name and self._last_name separated by a space.
        Since this is a method to get data only, I’ll add the @property
         decorator to our full_name method.
        """
        return f"{self._first_name} {self._last_name}"
