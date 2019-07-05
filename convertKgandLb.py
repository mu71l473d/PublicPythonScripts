#this script converts lb and kg

#imports the system module
import sys

print("this script converts lb and kg")
print("the first parameter should be kg or lb")

if len(sys.argv) == 2:
	if sys.argv[1] == "kg":
		print("this conversion will convert kg to lb")
		kg = float(raw_input("enter the amount in Kgs: "))
		lb = kg * 2.20462262
		print("Weight", kg, "KG = ", lb, "LB")
	
	elif sys.argv[1] == "lb":
		print("this conversion will convert lb to kg")
		lb = float(raw_input("enter the amount in lbs: "))
		kg = lb / 2.20462262
		print("Weight", lb, "LB = ", kg, "KG")
	
	else:
		print("invalid input")
	
else:
	print("you didn't put the right parameters in")
