#!/usr/bin/env python3

# Exercise 1. Split
 
import argparse

def not_int(value):
    try:
        int(value)
        raise argparse.ArgumentTypeError("Cannot be an interger.")
    except ValueError:
    	return value

def no_space(string_to_cut, string_separator):
	for char in string_to_cut:
		if char in string_separator:
			return string_to_cut
	else: 
		print("error, your string does't contain any space")
		exit()

        
def parse_arguments():
	parser = argparse.ArgumentParser(description='Process a string to return it with an uppercase at the begining of each word .')
	parser.add_argument('string_to_cut', type=not_int, help='The string you want to convert.')
	args = parser.parse_args()
	return args.string_to_cut

def split_string_by_space(string_to_cut, string_separator):
	table = []
	index_start = 0
	index_stop = 0 
	for char in string_to_cut:
		index_stop += 1 
		if char in string_separator:
			table.append(string_to_cut[index_start:index_stop - 1]) # -1 to avoid getting the " "
			index_start = index_stop
	table.append(string_to_cut[index_start:index_stop]) # we append the last part of our string, trigger once get out of our for loop
	return table

def main():
	#1 and #2. Handling errors and Parsing
	string_to_cut = parse_arguments()
	string_separator = " \n\t"
	no_space(string_to_cut, string_separator)

	# 3. Resolution
	splitted_string_table = split_string_by_space(string_to_cut, string_separator)
	
	# 4. Display
	print(*splitted_string_table, sep="\n")

if __name__ == "__main__":
	main()
