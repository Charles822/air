#!/usr/bin/env python3

# Exercise 2. Split en fonction (split accroding to a separator argument)
 
import argparse

def not_int(value):
    try:
        int(value)
        raise argparse.ArgumentTypeError("Cannot be an interger.")
    except ValueError:
    	return value

def no_separator(string_to_cut, string_separator):
	if string_separator not in string_to_cut: 
		print("error")
		exit()
      
def parse_arguments():
	parser = argparse.ArgumentParser(description='Process a string to return it with an uppercase at the begining of each word .')
	parser.add_argument('string_to_cut', type=not_int, help='The string you want to convert.')
	parser.add_argument('separator', type=not_int, help='The substring that will trigger the split.')
	args = parser.parse_args()
	return args.string_to_cut, args.separator

def split_string_by_separator(string_to_cut, separator):
	table = []
	index_start = 0
	index_stop = 0 
	for i in range(0,len(string_to_cut)):
		index_stop += 1 
		lenght_separator = len(separator)
		element = string_to_cut[i:i + lenght_separator]
		if element == separator:
			table.append(string_to_cut[index_start:index_stop - 1])
			index_start = index_stop + (lenght_separator - 1)
	table.append(string_to_cut[index_start:index_stop])
	return table

def main():
	#1 and #2. Handling errors and Parsing
	string_to_cut, separator = parse_arguments()
	no_separator(string_to_cut, separator)

	# 3. Resolution
	splitted_string_table = split_string_by_separator(string_to_cut, separator)
	
	# 4. Display
	print(*splitted_string_table, sep="\n")

if __name__ == "__main__":
	main()
