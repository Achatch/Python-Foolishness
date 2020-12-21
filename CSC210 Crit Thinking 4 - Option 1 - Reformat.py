'''This code takes in a date in string format, converts to a datetime object, and then outputs the date
    formatted as weekday, day/month/year'''

import datetime

monthsUpper = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
               "September": 9, "October": 10, "November": 11, "December": 12}
monthsLower = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8,
               "september": 9, "october": 10, "november": 11, "december": 12}


# Function to use above dict to convert string month to decimal month
def getmonth():
    print("Please input your month as a word. ex: january, february, etc")
    userMonth = input()
    if userMonth in monthsLower:
        month = monthsLower[userMonth]
        return month
    elif userMonth in monthsUpper:
        month = monthsUpper[userMonth]
        return month


# Function to get day of the week
def getday():
    day = input("Enter your day of the month ex: 5\n")
    return day


# Function to get year
def getyear():
    year = input("Please enter your year in four digits ex: 1991\n")
    return year


def main():
    month = str(getmonth())  # Convert int to string for later use
    year = getyear()
    day = getday()
    date = day + "/" + month + "/" + year  # Concatenate into one date time format string

    date_time = datetime.datetime.strptime(date, "%m/%d/%Y")  # Convert from string to datetime object
    dateFormatted = datetime.datetime.strftime(date_time,
                                               "%A, %m/%d/%Y")  # Convert from datetime object back to string in different format
    print(dateFormatted)  # Print new datetime string


if __name__ == '__main__':
    main()
