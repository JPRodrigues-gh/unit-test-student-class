""" Student test file """
import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """
    first test for our Student class.
    We created an instance of the class and asserted that the full_name
     method returns the correctly formatted student name.
    iow
    instantiated Student class and called the full_name method on it to
     assert whether it returned the first_name and last_name property
     values separated by a space
    """
    def test_full_name(self):
        """ Instance of student class """
        student = Student('John', 'Doe')

        # an assertEqual on the student instance to see whether
        # calling the full_name method on it returns the expected value
        self.assertEqual(student.full_name, 'John Doe')

    def test_alert_santa(self):
        """
        Test for a function called alert_santa that will change the
         naughty_list property to True. If a student misbehaves for
         some reason, we want to alert Santa by adding the student to
         his naughty list.
        """
        # Instance of student class
        student = Student('John', 'Doe')

        # student instance created, call the alert_santa method on it
        student.alert_santa()

        # Use assertTrue because we know that we want the alert_santa method
        #  to set the value of the naughty_list property to True when called
        # Note. we don’t pass a second argument to assertTrue as it’s not
        #  comparing two values but simply checking whether an expression or
        #  value is True
        self.assertTrue(student.naughty_list)


if __name__ == "__main__":
    # if statement so we can run the file without
    #  having to specify the unittest module.
    unittest.main()
