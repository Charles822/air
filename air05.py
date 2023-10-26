#!/usr/bin/env python3

# Exercise 6. Sur chacun d'entre eux / Over each element
 
import argparse

def is_int(value):
	try:
		return int(value)
	except ValueError:
		raise argparse.ArgumentTypeError("Arguments must be intergers.")

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process a list of integers and the last argument is the number to add.')
	parser.add_argument('inputs', nargs='+', type=is_int, help='A list of integers')
	parser.add_argument('operation_element', type=is_int, help='number to add on top of each argument.')
	args = parser.parse_args()
	return args.inputs, args.operation_element

def add_operation_on_each_element(arguments, operation_element):
	modified_list = []
	for argument in arguments:
		modified_list.append(argument + operation_element)
	return modified_list

def main():
	#1 and #2. Handling errors and Parsing
	arguments, operation_element = parse_arguments()

	# 3. Resolution
	modified_arguments = add_operation_on_each_element(arguments, operation_element)
	
	# 4. Display
	print(*modified_arguments, sep=" ")

if __name__ == "__main__":
	main()
