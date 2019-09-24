#!/usr/bin/env python3

##Work in progress, might not work completely


input_str = input("Enter the string that you like to be base64 encoded:")
times = int(input("How deep do you want it encoded:"))

output_str = input_str

for i in range(times):
	output_str = output_str.encode("base64")

print("Encoded string: ", output_str)
