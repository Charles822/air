#!/usr/bin/env python3

# Exercise 10. Rotation vers la gauche / Rotate to the left
 
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a list of values.")
    parser.add_argument('original_list', nargs='+', help='A list of values of any type')
    args = parser.parse_args()
    return args.original_list

def rotate_elements_left(original_list):
	new_table = original_list
	lenght = len(new_table)
	for num in range(0, lenght - 1):
		next_num = num + 1
		new_table[num], new_table[next_num] = new_table[next_num], new_table[num]
	return new_table # we could have simply used the sorted() function


def main():
	#1 and #2. Handling errors and Parsing
	original_list = parse_arguments()
	

	# 3. Resolution
	rotated_table = rotate_elements_left(original_list)
	
	# 4. Display
	print(*rotated_table, sep=", ")

if __name__ == "__main__":
	main()
