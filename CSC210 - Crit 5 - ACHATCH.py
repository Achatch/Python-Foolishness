'''Write a program in Python which uses a while loop to sum the squares of integers
(starting from 1) until the total exceeds 200.
Print the final total and the last number to be squared and added.'''

i = 0  # Initialize iterator variable
total = int(input('Enter the value you would like to exceed\n'))
for square in range(0, total):  # Initialize range
    if i < 200:
        i = i + (square * square)  # Add iterator to itself, plus squared value until iterator is greater than 200.
    else:
        # Print the square
        print("The last value square was " + str(square - 1))
        #  Print the iterator
        print("The final amount is: " + str(i))
        break