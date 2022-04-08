import pandas as pd
import os

Raw = input("Name of RawData.csv: ")
RawName = Raw + '.csv'
df = pd.read_csv(RawName, parse_dates=['TradingDate'])
print(df.info())
input("Enter Any Key To Continue...")

path = './' + Raw
if not os.path.exists(path):
    os.makedirs(path)
    print("File Folder Created in " + path)
else:
    print("File Folder Detected in " + path)

FileName = './' + Raw + '/' + '{}{:0>2}{:0>2}.csv'
print("Processing...")
Count = 0
for year in df.TradingDate.apply(lambda x: x.year).unique():
    for month in df.TradingDate.apply(lambda x: x.month).unique():
        for day in df.TradingDate.apply(lambda x: x.day).unique():
            view = df[df.TradingDate.apply(lambda x: x.day == day and x.month == month and x.year == year)]
            if view.size:
                view.to_csv(FileName.format(year, month, day))
                Count = Count+1

print("All Done for " + Count + "File(s)")
input("Enter Any Key To End")
