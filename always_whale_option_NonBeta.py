import pandas as pd
import csv

Location = r'C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\preferences\STSPlayer'
Location2 = r'C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\preferences\test'

df1 = pd.read_csv(Location,skiprows=1,sep=':', header=None)
df1=df1.drop(df1.index[[6]])

#if "0" in df1.iat[6,1]:
#    df1.iat[6,1]=' "1"'
    
if "0" in df1.iloc[4,1]:
    df1.iat[4,1]=' "1",'
#    
if "0" in df1.iloc[5,1]:
    df1.iat[3,1]=' "1",'

df1.to_csv(Location2, sep=':', index=False, header=False, quoting=csv.QUOTE_NONE)

lst1=['{']
    
with open(Location2) as f:
    lst2=f.read().splitlines()

for x in range(len(lst2)):
    lst1.append(lst2[x])

lst1.append('}')

with open(Location, 'w') as filehandle:  
    for listitem in lst1:
        filehandle.write('%s\n' % listitem)

