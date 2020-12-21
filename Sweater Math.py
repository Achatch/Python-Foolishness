'''This script takes user inputted measurement variables
to output the necessary information used to make a sweater
TODO: Add more sweater types.
'''

print('How many stitches per inch?')
Stitches_inch = int(input())
print('How many stitches per row?')
Stitches_row = int(input())
print('Bust Measurement')
Bust = int(input())
print('Is there an Ease for Bust? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for Bust value')
    Bust = Bust + int(input())
    print('Bust is now '+str(Bust))
print('Back of Neck Measurement')
BackNeck = int(input())
print('Is there an Ease for the Back of Neck? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for the Back of Neck value')
    BackNeck = BackNeck + int(input())
    print('Back of Neck is now '+str(BackNeck))
print('Upper arm circumference measurement')
UACirc = int(input())
print('Is there an Ease for the Upper Arm Circumference? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for Upper Arm Circumference value')
    UACirc = UACirc + int(input())
    print('Upper Arm Circumference is now '+str(UACirc))
print('Wrist Circumference measurement')
WriCirc = int(input())
print('Is there an Ease for the Wrist Circumference? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for Wrist Circumference value')
    WriCirc = WriCirc + int(input())
    print('Wrist Circumference is now '+str(WriCirc))
print('Yoke Depth Mesurement')
YokeDepth=int(input())
print('Is there an Ease for the Yoke Depth? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for Yoke Depth value')
    YokeDepth = YokeDepth + int(input())
    print('Yoke Depth is now '+str(YokeDepth))
print('Arm Length measurement')
ArmLength=int(input())
print('Is there an Ease for the Arm Length? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for Arm Length value')
    ArmLength = ArmLength + int(input())
    print('Arm Length is now '+str(ArmLength))
print('Waist Circumference measurement')
WaistCirc=int(input())
print('Is there an Ease for the Waist Circumference? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for Waist Circumference value')
    WaistCirc = WaistCirc + int(input())
    print('Waist Circumference is now '+str(WaistCirc))
print('Neck to waist measurement')
NecktoWaist=int(input())
print('Is there an Ease for the Neck to Waist? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for Neck to Waist value')
    NecktoWaist = NecktoWaist + int(input())
    print('Neck to Waist is now '+str(NecktoWaist))
print('Body length measurement')
BodyLength=int(input())
print('Is there an Ease for the Body Length? (Y/N)')
if str(input()) == 'Y':
    print('Enter your Ease for Body Length value')
    BodyLength = BodyLength + int(input())
    print('Body Length is now '+str(BodyLength))
print('What kind of sweater are we making?\nAcceptable inputs are:\n\tpullover\n\t')
sweatertype = input()
WaistChangeStart = NecktoWaist - YokeDepth
'''Below is for pullovers only'''

# Function for pullover SweaterMath
def pullover():
    # TODO: Full yoke has to be an even number if the cast on is an even number
    # TODO: Output variables are CastOn variables, rename all
    # TODO: Full yokes need to be even if caston is even
    backOutput = round((BackNeck)*Stitches_inch)
    frontOutput = round((BackNeck)*Stitches_inch)
    sleeveOutput = round((BackNeck*Stitches_inch*0.3))
    totalOutput = round(sleeveOutput*2+frontOutput+backOutput)

    print('Back: '+str(backOutput)+'\nFront: '+str(frontOutput)+'\nSleeve: '+str(sleeveOutput)+'\n+Total: '+str(totalOutput))

    # determining full yoke depth, how many rows to yoke depth

    fyd = round(YokeDepth*Stitches_row)
    increases = int((fyd/2))
    print('this is your full yoke depth: '+str(fyd))
    print('You can only increase every other row, you have '+str(increases)+' rows available for increase')
    #T ODO: Add ease_b variable per full/output variables, add after calculation//Replace float wth round
    Fullback = round(Bust*Stitches_inch*.5)
    FullFront = round(Bust*Stitches_inch*.5)
    FullSleeve = round(UACirc*Stitches_inch)

    print('Full yoke stitches:\nBack: '+str(Fullback)+'\nFront: '+str(FullFront)+'\nSleeve: '+str(FullSleeve))
    TotalFullYoke = (FullSleeve+FullSleeve+Fullback+FullFront)
    print('Total: '+str(float(TotalFullYoke)))


    increaseStartfront = abs(frontOutput - increases)
    increaseStartback = abs(backOutput - increases)
    increaseStartsleeves = abs(sleeveOutput - increases)
    'increases:'
    print('Start increases in the front on this stitch: '+str(increaseStartfront)+
          '\nStart increases in the back on this stitch: '+str(increaseStartback)+
          '\nStart increases on the sleeves on this stitch: '+str(increaseStartsleeves)+
          '\nCast on four, separate the sleeve, cast on four, separate the sleeve')

    # This is Optional, some do not want to pinch in or come out, may want to go straight
    print('Once you get to '+str(WaistChangeStart)+' inches\n'
          'If you want to decrease your waist\n'
          'Starting from the right front: \bssk k across k 2 tog sm ssk k across ssk\b\n'
          'Defines the decrease round\n'
          'knit next round\n'
          'Decrease rounds as needed\n'
          'Knit to '+str(BodyLength)+' inches and cast off\n'
          'Put sleeve stitches back on\n'
          'Then pick up sleeves\n')
    # Calculates the sleeve taper from UA circ to Wrist Circ
    sleeves = round(ArmLength * Stitches_row)
    '''distritbue decreasese evenly until down to 34
        gradually can do up to 2
        '''
    wrist = round(WriCirc * Stitches_inch)
    '''Fullsleeve - 4 cause there are reasons (ask mom)
        60-wrist
        26
        34(wrist)/2 (2 decreases at a time). Sleeves divided by that is how to gradually decrease'''
    print(wrist, sleeves)
    # calculates when to decrease for sleeves to make the correct circumference
    print('You should decrease every ' +str(int(sleeves/(wrist/2))) + ' stitches to end up with a wrist circumference'
                                                                      ' of '+str(WriCirc))

if sweatertype == 'pullover':
    pullover()

'''increases to skip
skipsfront = (increases - (FullFront - frontOutput)/2)
skipsback = (increases - (Fullback - backOutput)/2)
skipssleeves = (increases - (FullSleeve - sleeveOutput)/2)

print()
Math is number of increases - (number to add/2) ex: 94 full yoke, 44 cast on, 50 remaining, 31 increases availables (31 - (50/2) = 6'''

'''Differences betweeen Cast on and Full Yoke
Determines how many stitches you have left
To get to the full yoke stitch
Distribute this between the fullyoke depth divided by two
as evenly as possible

Ex: 44 cast on, 94 full yoke, leave 31 free stitches to get to 94 where do I start?'''
''''subtracting the number of body increases from the individual sections

Need 50
31 Opps
Have 44
End is 94

31-25 = 7 increases to skip for the back and front
Skip every fourth increase for the back and the front

Need 44
Have 12
End is 56
31 opps
31 - 22 = 9 increases to skip for the sleeves
Skip every third increase for the back and the front'''

