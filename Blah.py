array = []
numberOfNouns = 6
numberOfAdverbs = 1
numberOfPluralNouns = 1
numberOfAdjectives = 3
adjectives = []
nouns = []
adverbs = []
pluralNouns = []
while numberOfNouns != 0:
    print('please enter a noun, you have '+str(numberOfNouns)+' nouns remaining')
    nouns.append(input())
    numberOfNouns = numberOfNouns - 1
while numberOfPluralNouns != 0:
    print('please enter a Plural Noun, you have '+str(numberOfPluralNouns)+' Plural Nouns remaining')
    pluralNouns.append(input())
    numberOfPluralNouns = numberOfPluralNouns - 1
while numberOfAdverbs != 0:
    print('please enter an adverb, you have '+str(numberOfAdverbs)+' adverb remaining')
    adverbs.append(input())
    numberOfAdverbs = numberOfAdverbs - 1
while numberOfAdjectives != 0:
    print('please enter an adjective, you have '+str(numberOfAdjectives)+' adjective remaining')
    adjectives.append(input())
    numberOfAdjectives = numberOfAdjectives - 1
madlib = 'Driving a car can be fun if you follow this ' + str(adjectives[0])+' advice: ' \
        'When approaching a '+ str(nouns[0])+' on the right, always blow your ' + str(nouns[1])+'. ' \
        'Before making a '+str(adjectives[1])+' turn, always stick your ' + str(nouns[2])+' out of the window. ' \
        'Every 2000 miles, have your '+ str(nouns[3])+' inspected and your ' + str(nouns[4])+' checked. ' \
        'When approaching a school, watch out for '+str(adjectives[1])+ ' ' + str(pluralNouns[0])+'. '  \
        'Above all, drive '+ str(adverbs[0])+'.  The '+ str(nouns[5])+' you save may be your own!'
print(madlib)

