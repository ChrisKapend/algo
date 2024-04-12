def is_leap(year):
    """Check whether year is a leap year. or no
    it takes as an input a year and returns True or False if the year is a leap year or no"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 🚨 Do NOT change any of the code below
year_ = int(input("Enter a year: "))
month_ = int(input("Enter a month: "))
days_ = days_in_month(year_, month_)
print(days_)

print(is_leap(2024))