""" Check for leap year """


class GetLeapYear:
    """ Check for leap year """

    def __init__(self, year):
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            # print("leap year has 366 days")
            self.days = 366
        else:
            # print("Not a leap year therefore has 365 days")
            self.days = 365

    # year = GetLeapYear(1900)
    # print ( 1900, "is a leap year"
    # if is_leap_year(1900) else "is not a leap year")
