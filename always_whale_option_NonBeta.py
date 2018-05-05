Location = r'C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\preferences\STSPlayer'

with open(Location) as f:
    lst2=f.read().splitlines()

for x in range(len(lst2)):
    if '"0"' in lst2[x]:
        lst2[x]=lst2[x].replace('"0"','"1"')

with open(Location, 'w') as filehandle:  
    for listitem in lst2:
        filehandle.write('%s\n' % listitem)

