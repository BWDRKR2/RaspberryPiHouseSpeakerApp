import json

with open('dan2data.json', 'r') as f:
        relays_dict = json.load(f)



count = 0
for room in relays_dict['ROOMS']:
        
        active = (room["Active"])
        #print room 

        print relays_dict
        print "*****"
	if active == "Y":
		print "Active"
	else:
		del relays_dict["ROOMS"][count]
		print "Not Active"
                print "Count = ",count
        count = count + 1
print relays_dict

