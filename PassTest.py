import pandas as pd
pw = '0H9T9L9K6V'
df = pd.read_csv('output.csv')
df1 = df['Category_0']

df2 = df.loc[df['Category_0'] == pw]

if len(df2 != 0):
    print('duplicate {}'.format(pw))
