
Location = r'C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\betaPreferences\STSPlayer'
    
with open(Location) as f:
    lst2=f.read().splitlines()

lst2[7]=lst2[7].replace("0","1")
lst2[5]=lst2[5].replace("0","1")
lst2[4]=lst2[4].replace("0","1")

with open(Location, 'w') as filehandle:  
    for listitem in lst2:
        filehandle.write('%s\n' % listitem)
