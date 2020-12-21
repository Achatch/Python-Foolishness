'''The Daily Trumpet newspaper accepts classified advertisements in 15 categories
Ex: Apartments for Rent, Pets for Sale, etc.
Develop the logic for a program that accepts classified advertising data
Including category code
Category Code = integer 1-15
And the number of words in the ad.
Store these values in parallel arrays
Sort the arrays so that the records are sorted in ascending order by category
Output lists:
Category Number
Number of ads
Total number of words in ads
'''
#  Create category prompt for later use
categoryPrompt = ('Please choose your classified advertising category, or 0 to exit\n'
                  'Enter 1 for Apartments for Rent\n'
                  'Enter 2 for Pets for Sale\n'
                  'Enter 3 for Cars for Sale\n'
                  'Enter 4 for Job Openings\n'
                  'Enter 5 for Furniture Sales\n'
                  'Enter 6 for lost Pets\n'
                  'Enter 7 for category seven\n'
                  'Enter 8 for category eight\n'
                  'Enter 9 for category nine\n'
                  'Enter 10 for category ten\n'
                  'Enter 11 for category eleven\n'
                  'Enter 12 for category twelve\n'
                  'Enter 13 for category thirteen\n'
                  'Enter 14 for category fourteen\n'
                  'Enter 15 for category fifteen\n')

#  Create category arrays
apartmentsRent,petsForSale,carsForSale,jobOpenings,furnitureSales,lostPets,categorySeven,categoryEight,categoryNine,categoryTen,categoryEleven,categoryTwelve,categoryThirteen,categoryFourteen,categoryFifteen = ([] for i in range(15))

# Create the count of advertisement array
adCountArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Array of Category Names for pretty text
categoryNames = ['Buffer','Apartments for Rent','Pets for Sale','Cars for Sale','Job Openings','Furniture Sales','Lost Pets','Category Seven','Category Eight','Category Nine','Category Ten','Category Eleven','Category Twelve','Category Thirteen','Category Fourteen','Category Fifteen']

# Dict of Arrays
options = {1:apartmentsRent,
           2:petsForSale,
           3:carsForSale,
           4:jobOpenings,
           5:furnitureSales,
           6:lostPets,
           7:categorySeven,
           8:categoryEight,
           9:categoryNine,
           10:categoryTen,
           11:categoryEleven,
           12:categoryTwelve,
           13:categoryThirteen,
           14:categoryFourteen,
           15:categoryFifteen}

# Counter and determining variables for later use, global variables.
optionChoice = -1
dataChoice = -1


#  Fat Finger Checker checks to ensure the correct category option was chosen
def fatFingerChecker(categoryChosenPrettyName):
    print('You have chosen '+categoryChosenPrettyName+', is this correct? (Y/N)')
    ffAnswer = input()
    i = 0
    if ffAnswer == 'N':
        main()
    return i

# Function to enter data to the appropriate array
def enterData(categoryChosenPrettyName,optionChoice):
    i = 1
    while i != 0:
        print('Please enter your '+categoryChosenPrettyName+' advertisement word count')
        adWordCount = int(input())
        options[optionChoice].append(adWordCount)
        # Sorts the data each time you enter a value
        adCountArray[optionChoice] = adCountArray[optionChoice] + 1
        print('To enter another value, press 1, to return to the previous menu, press 0')
        i = int(input())
        if 0 > i < 1:
            print('Invalid Value.\nTo enter another value, press 1, to return to the previous menu, press 0')
    return

#  Function to view data stored in appropriate array
def viewData(categoryChosenPrettyName,optionChoice):
    totalCount = 0
    for item in options[optionChoice]:
        totalCount = totalCount + item
    print('\t\t**** Current Data for '+categoryChosenPrettyName+' ****\n'
          'Category Number:' + str(optionChoice) + '\n'
          'Number of Ads:' + str(adCountArray[optionChoice]) + '\n'
          'Total Word Count:' + str(totalCount) + '\n')
    return

def optionMaker():
    print(categoryPrompt)
    optionChoice = int(input())
    if (optionChoice<0) or (optionChoice>15):  # Invalid values unacceptable
        print('Invalid Value, please try again\n')
        main()
    if optionChoice == 0:
        exit()
    categoryChosenPrettyName = categoryNames[optionChoice]
    categoryChosenArrayName = options[optionChoice]
    fatFingerChecker(categoryChosenPrettyName)
    return categoryChosenPrettyName, categoryChosenArrayName, optionChoice

def dataChooser(categoryChosenPrettyName, optionChoice):
    print('If you would like to enter data for ' + categoryChosenPrettyName + ' enter 1, to view data, enter 2, to return to the previous menu, enter 0')
    dataChoice = int(input())
    if dataChoice == 1:
        enterData(categoryChosenPrettyName,optionChoice)
    elif dataChoice == 2:
        viewData(categoryChosenPrettyName,optionChoice)
    elif dataChoice == 0:
        return(dataChoice)
    else:
        print('Please enter a valid value. To add data, enter 1, to view data enter 2, to return to the category select, enter 0')

# Main function
def main():
    optionChoice = -1
    while optionChoice != 0:
        dataChoice = -1
        optionMakerOutput = optionMaker()
        categoryChosenPrettyName = optionMakerOutput[0]
        optionChoice = optionMakerOutput[2]
        while dataChoice != 0:
            dataChoice = dataChooser(categoryChosenPrettyName,optionChoice)
    exit()

if __name__ == '__main__':
    main()
