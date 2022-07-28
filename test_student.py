""" Student test file """
import unittest
from unittest.mock import patch
from datetime import timedelta
# from leap_year import GetLeapYearfor
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
    # adding the @classmethod decorator to a method and passing ‘cls’ as a
    # method parameter will make it a class method which acts on the class
    # instead of an instance of the class
    #
    # Use the setUpClass method to run code once at the beginning of our tests
    # For example, we may want to do this to populate a test database with data
    # @classmethod
    # def setUpClass(cls):
    #     print('setUpClass')

    # use the tearDownClass method to run code once at the end of our tests
    # For example, to destroy a test database
    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')

    # setUp method gets called before each test method
    # Use setUp method to instantiate the Student class once
    # instead of in each test method
    def setUp(self):
        # print('setUp')
        self.student = Student('John', 'Doe')

    # tearDown method gets called after each test method
    # def tearDown(self):
        # print('tearDown')

    def test_full_name(self):
        """ Test full_name function that will return a students full name """
        # Instance of student class
        # student = Student('John', 'Doe')
        # print('test_full_name')

        # an assertEqual on the student instance to see whether
        # calling the full_name method on it returns the expected value
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        """
        Test for a function called alert_santa that will change the
         naughty_list property to True. If a student misbehaves for
         some reason, we want to alert Santa by adding the student to
         his naughty list.
        """
        # Instance of student class
        # student = Student('John', 'Doe')
        # print('test_alert_santa')

        # student instance created, call the alert_santa method on it
        self.student.alert_santa()

        # Use assertTrue because we know that we want the alert_santa method
        #  to set the value of the naughty_list property to True when called
        # Note. we don’t pass a second argument to assertTrue as it’s not
        #  comparing two values but simply checking whether an expression or
        #  value is True
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        """
        Assert whether email method returns expected email address output of
         _first_name dot _last_name@email.com
        """
        # Instance of student class
        # student = Student('John', 'Doe')
        # print('test_email')

        # an assertEqual on the student instance to see whether
        # calling the email method on it returns the expected value
        self.assertEqual(self.student.email, 'john.doe@email.com')
        # self.assertEqual(student.email,
        #              '{student._first_name}.{student._last_name}@email.com')

    def test_apply_extension(self):
        """
        Assert whether student’s end_date is equal to the old date plus
         a timedelta of five days
        """
        # Instance of student class
        # student = Student('John', 'Doe')
        # print('test_apply_extension')
        old_end_date = self.student.end_date
        # print(old_end_date)
        self.student.apply_extension(5)

        # an assertEqual on the student instance to see whether
        # calling the email method on it returns the expected value
        self.assertEqual(self.student.end_date, old_end_date + timedelta
                         (days=5))

    def test_course_schedule_success(self):
        """ test course_schedule function for success"""
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        """ test course_schedule function for failure"""
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")


if __name__ == "__main__":
    # if statement so we can run the file without
    #  having to specify the unittest module.
    unittest.main()
