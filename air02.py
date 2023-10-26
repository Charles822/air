#!/usr/bin/env python3

# Exercise 3. Concat (Concatenate)
 
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process an arbitrary number of arguments.')
	parser.add_argument('array_of_strings', nargs='+', help='Input arguments.')
	parser.add_argument('separator', help='The substring that will trigger the split.')
	args = parser.parse_args()
	return args.array_of_strings, args.separator
      
def concatenate_in_one_string(array_of_strings, separator):
	one_string = ""
	for element in array_of_strings:
		one_string += element + separator
	return one_string
	
def main():
	#1 and #2. Handling errors and Parsing
	array_of_strings, separator = parse_arguments()

	# 3. Resolution
	formatted_string = concatenate_in_one_string(array_of_strings, separator)
	
	# 4. Display
	print(formatted_string)

if __name__ == "__main__":
	main()
