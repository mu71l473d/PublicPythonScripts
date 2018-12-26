#this script converts kph and mph

#import the sys module
import sys

print "this script converts kmh and mph, the first parameter should always be the unit you want to convert: kmh or mph"

if len(sys.argv) == 2:
	if sys.argv[1] == "mph":
		mph = float(raw_input("Enter mp/h: "))
		kph = mph / 0.6214 
		print "Speed:", mph, "MP/H = ", kph, "KPH"
	elif sys.argv[1] == "kph":
		kmh = float(raw_input("Enter km/h: "))
		mph =  0.6214 * kmh
		print "Speed:", kmh, "KM/H = ", mph, "MPH"
	else:
		print "invalid input"
else:
	print "you didn't input the right parameters for this script to work"
