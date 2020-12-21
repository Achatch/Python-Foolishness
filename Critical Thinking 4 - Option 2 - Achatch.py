"""The current tuition is $20,000 per year
tuition is expected to increase by 3 percent each year.
Display the tuition each year for the next 10 years."""
collegeTuition = 20000  # Set current tuition variable
increase = .03  # set tuition increase variable
year = int(2020)  # set year at 2020, year doubles as iterator
while year < 2031:  # loop to continue until ten years has passed
    print('Hunterville College Tuition for ' + str(year) + ': $'+str(round(collegeTuition, 2)) + ' per year')  # Display value formatted to taste rounded to 2 decimal places
    collegeTuition = float(collegeTuition * increase + collegeTuition)  # Calculates tuition based on 3% increase
    year = year + 1  # iterate year forward, max at 11 years (initial year + 10 years)
