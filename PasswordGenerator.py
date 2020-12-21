import random
rn = {0:'2', 1:'3', 2:'3', 3:'5', 4:'5', 5:'6', 6:'7', 7:'9'}
ra = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 33:'H', 17:'J', 18:'K', 19:'L', 20:'M', 21:'N', 22:'P', 23:'Q', 24:'R', 25:'S', 26:'T', 27:'U', 28:'V', 29:'W', 30:'X', 31:'Y', 32:'Z'}
print('Enter the amount of categories you have')
categories = int(input())
print('Enter how many respondents you have per category')
respondants = int(input())
print('Enter how many characters you would like per ID')
characters = int(input())
total = []
ccnt = categories
categories = categories + 1
while categories != 1:
    out = []
    respcounter = 0
    while (respondants != respcounter):
        respcounter = respcounter + 1
        pw = str(categories)
        counter = 0
        while (counter != characters):
            counter = counter + 1
            if counter % 2 == 0:
                pw = pw + rn[random.randint(0,7)]
            if counter % 2 == 1:
                pw = pw + ra[random.randint(10,33)]
        for item in out:
            if pw == item:
                print('removing duplicate ' + pw)
                out.remove(pw)
                respcounter = respcounter - 1
        out.append(pw)
    total.append(out)
    categories = categories - 1
towrite = (zip(*total))
with open('IDgen.csv', 'w+') as outfile:
    for line in towrite:
        i = 0
        while ccnt != i:
            outfile.write(line[i]+',')
            i = i + 1
        outfile.write('\n')