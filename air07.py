#!/usr/bin/env python3

# Exercise 8. Insertion dans tableau trié / Insetion within an sorted table
 
import argparse

def is_int(value):
	try:
		return int(value)
	except ValueError:
		raise argparse.ArgumentTypeError("Arguments must be intergers.")

def is_sorted(ascending_list):
	if ascending_list == sorted(ascending_list): # if we wanted to avoid the buil in sorted function we could use a buble sort for instance
		return ascending_list
	else:
		print("Arguments are not in ascending order.")
		exit()


def parse_arguments():
	parser = argparse.ArgumentParser(description='Process a list of integers in ascending order.')
	parser.add_argument('ascending_list', nargs='+', type=is_int, help='A list of intergers in ascending order')
	parser.add_argument('number_to_add', type=is_int, help='an integer to add to our ascending list.')
	args = parser.parse_args()
	return args.ascending_list, args.number_to_add

def add_number_in_ascending_order(ascending_list, number_to_add):
	list_with_extra_number = []
	for number in ascending_list:
		if number <= number_to_add:
			list_with_extra_number.append(number)
		else:
			list_with_extra_number.append(number_to_add)
			list_with_extra_number.append(number)
			number_to_add = ascending_list[-1] + 1 # in this way we ensure that our number_to_add doesn't get printed again, number cannot be greater anymore
	return list_with_extra_number

def main():
	#1 and #2. Handling errors and Parsing
	ascending_list, number_to_add = parse_arguments()
	is_sorted(ascending_list)

	# 3. Resolution
	list_with_extra_number = add_number_in_ascending_order(ascending_list, number_to_add)
	
	# 4. Display
	print(*list_with_extra_number, sep=" ")

if __name__ == "__main__":
	main()
