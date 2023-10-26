#!/usr/bin/env python3

# Exercise 9. Mélanger deux tableaux triés / Merge two sorted tables
 
import argparse

def is_sorted(table):
	if table == sorted(table): # if we wanted to avoid the build in sorted function we could use a buble sort for instance
		return table
	else:
		print(f"{table} is not in ascending order.")
		exit()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process 2 lists of integers in ascending order and the word 'fusion' to seperate them.")
    parser.add_argument('input', nargs='+', help='A list of intergers in ascending order separated by a fusion element')
    args = parser.parse_args()

    try:
        fusion_index = args.input.index('fusion')
    except ValueError:
    	print("error: fusion not found in input")
    	exit()
    fusion = args.input[fusion_index]

    try:
        ascending_list_one = [int(i) for i in args.input[:fusion_index]]
    except ValueError:
    	print("error: ascending_list_one element cannot be converted into intergers")
    	exit()

    try:
        ascending_list_two = [int(i) for i in args.input[fusion_index + 1:]]
    except ValueError:
    	print("error: ascending_list_two element cannot be converted into intergers")
    	exit()
    
    return ascending_list_one, fusion, ascending_list_two


def merge_tables(ascending_list_one, ascending_list_two):
	merged_tables = ascending_list_one + ascending_list_two # we merge the 2 tables and we use the sorting algorythm
	lenght = len(merged_tables)
	for i in range(0, lenght - 1):
		min = i
		for j in range(i + 1, lenght):
			if merged_tables[j] < merged_tables[min]:
				min = j
		if min != i:
			merged_tables[i], merged_tables[min] = merged_tables[min], merged_tables[i]
	return merged_tables # we could have simply used the sorted() function

def main():
	#1 and #2. Handling errors and Parsing
	ascending_list_one, fusion, ascending_list_two = parse_arguments()
	is_sorted(ascending_list_one)
	is_sorted(ascending_list_two)

	# 3. Resolution
	new_table = merge_tables(ascending_list_one, ascending_list_two)
	
	# 4. Display
	print(*new_table, sep=" ")

if __name__ == "__main__":
	main()
