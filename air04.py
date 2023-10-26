#!/usr/bin/env python3

# Exercise 5. Un seul à la fois / One at a time
 
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process a string.')
	parser.add_argument('string_to_change', help='Input argument.')
	args = parser.parse_args()
	return args.string_to_change

def delete_repeating_char(string_to_change):
	lenght = len(string_to_change)
	new_string = ""
	for index in range(0, lenght):
		if string_to_change[index] == string_to_change[index - 1]:
			pass
		else: 
			new_string += string_to_change[index]
	return new_string
		
def main():
	#1 and #2. Handling errors and Parsing
	string_to_change = parse_arguments()

	# 3. Resolution
	no_repeat_string = delete_repeating_char(string_to_change)
	
	# 4. Display
	print(no_repeat_string)

if __name__ == "__main__":
	main()
