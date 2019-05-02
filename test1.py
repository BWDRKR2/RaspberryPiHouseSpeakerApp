import json



#### Read All JSON


with open('dan2data.json') as f:
    data = json.load(f)
##print(data['ROOMS'])
##print('-----------')
##print('      ')
# Initalize Pins
for room in data['ROOMS']:
        #room['Relay_1'] = room['Relay_1'] + " ***"
	print"Room Desc : ", room['Room_Desc']
	print(room['Relay_1'])
	print(room['Relay_2'])
        print(" ")
	

#### Read By Room # 


get_Room_Num = '3'

g = next(item for item in data['ROOMS'] if item["Room_Num"] == get_Room_Num)


a = "ON"
b = "OFF"

if a == "ON" and b == "ON" :
	g['Status'] = "On"
else:
	g['Status'] = "Off"




print " "
print "G = ", g
print " "
print g["Relay_1"]
print g["Relay_2"]
print " "
print g["Status"]


