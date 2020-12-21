import os, random, datetime
import pandas as pd

df = pd.DataFrame()

rn = {0:'2', 1:'3', 2:'3', 3:'5', 4:'5', 5:'6', 6:'7', 7:'9'}
ra = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 33:'H', 17:'J', 18:'K', 19:'L', 20:'M', 21:'N', 22:'P', 23:'Q', 24:'R', 25:'S', 26:'T', 27:'U', 28:'V', 29:'W', 30:'X', 31:'Y', 32:'Z'}
print('Enter the amount of categories you have')
categories = int(input())
print('Enter how many respondents you have per category')
respondants = int(input())
print('Enter how many characters you would like per ID')
characters = int(input()) - 1

def duplicate_check(pw, df, header):
    df2 = df.loc[df[header] == pw]
    if len(df2 != 0):
        print('duplicate {}'.format(pw))
        return False
    else:
        return True


def password_create(pw, characters, header):
    counter = 0
    newpw = pw
    while counter < characters:
        counter += 1
        if counter % 2 == 0:
            newpw = newpw+rn[random.randint(0,7)]
        if counter % 2 == 1:
            newpw = newpw + ra[random.randint(10,33)]
    if duplicate_check(newpw, df, header) == True:
        return newpw
    else:
        password_create(pw, characters, header)
i = 1
while i < categories+1:
    respcount = 1
    df['Category_'+str(i)] = ''
    print('working category {}, time start:{}'.format(i, datetime.datetime.now()))
    header = 'Category_'+str(i)
    passwordarray = []
    while respondants > respcount:
        pw = str(i)
        pw = password_create(pw, characters, header)
        df.loc[respcount, header] = pw
        respcount += 1
    i+=1
df.to_csv('output.csv')