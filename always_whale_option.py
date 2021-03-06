import json

Location = r'C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\betaPreferences\STSPlayer'

with open(Location) as f:
    data = json.load(f)

for key, value in data.items():
    if value == '0':
        data[key] = '1'

with open(Location, 'w') as outfile:
    json.dump(data, outfile, indent=1)
