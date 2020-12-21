import pandas as pd
import calendar, time
df1 = pd.read_csv('500k_US_Accidents.csv')
i = 0
count = 0
ref_time = "2016-02-08 07:44:26"
refEpoch = calendar.timegm(time.strptime(ref_time, "%Y-%m-%d %H:%M:%S"))
while i < len(df1):
    accidentTime = df1.loc[i, "Start_Time"]
    accidentEpoch = calendar.timegm(time.strptime(accidentTime, "%Y-%m-%d %H:%M:%S"))
    if accidentEpoch in range((refEpoch - 1800), (refEpoch + 1800)):
        count = count + 1
    i = i + 1
print(count)