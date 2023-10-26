#!/usr/bin/env python3

# Exercise 7. Controle de pass sanitaire / Health pass control
 
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process a list of strings and string comparator.')
	parser.add_argument('list_of_strings', nargs='+', help='A list of strings')
	parser.add_argument('string_comparator', help='to check if this string is in each element of our list of strings.')
	args = parser.parse_args()
	return args.list_of_strings, args.string_comparator

def revert_elements_containing_string_comparator(list_of_strings, string_comparator):
	modified_list = []
	for string in list_of_strings:
		if string_comparator.lower() not in string.lower():
			modified_list.append(string)
		else:
			pass
	return modified_list

def main():
	#1 and #2. Handling errors and Parsing
	list_of_strings, string_comparator = parse_arguments()

	# 3. Resolution
	new_list = revert_elements_containing_string_comparator(list_of_strings, string_comparator)
	
	# 4. Display
	print(*new_list, sep=", ")

if __name__ == "__main__":
	main()
