import json

with open('dan2data.json') as f:
    data = json.load(f)
##print(data['ROOMS'])
##print('-----------')
##print('      ')
# Initalize Pins
for room in data['ROOMS']:
	print"Room Desc : ", room['Room_Desc']
	print(room['Relay_1'])
	print(room['Relay_2'])
        print(" ")
	# GPIO.setup(room['Relay_1'], GPIO.OUT)
	# GPIO.output(room['Relay_1'], GPIO.HIGH)
	# GPIO.setup(room['Relay_2'], GPIO.OUT)
	# GPIO.output(room['Relay_2'], GPIO.HIGH)

get_Room_Num = '1'
# Get Relays for room
#g = next(item for item in data['ROOMS'] if item["Room_Num"] == "2")
g = next(item for item in data['ROOMS'] if item["Room_Num"] == get_Room_Num)

print('-----------')
print(' g ')
print(g)
print('-----------')

myroom = g['Room_Num']
relay1 = g['Relay_1']
relay2 = g['Relay_2']

print('**********')
print(' ROOM ' + myroom)
print('-----------')

print('   relay 1 : ' + relay1)

print('**********')

print('   relay 2 : ' + relay2)

print('**********')
