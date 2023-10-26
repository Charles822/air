#!/usr/bin/env python3

# Exercise 12. Afficher une pyramide / Display a pyramid
 
import argparse

def is_int(value):
	try:
		return int(value)
	except ValueError:
		raise argparse.ArgumentTypeError("Your second argument must be an integer.")

def is_single_character(value):
	try:
		value[1]
		raise argparse.ArgumentTypeError("Your first argument must be a single character.")
	except IndexError:
		return value


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a character and a number of floors.")
    parser.add_argument('character', type=is_single_character, help='Any character')
    parser.add_argument('number_of_floors', type=is_int, help='number')
    args = parser.parse_args()
    return args.character, args.number_of_floors

def create_floors_list(character, number_of_floors):
	pyramid_floors = []
	char_number = 1
	for floor in range(1, number_of_floors + 1):
		space_number = " " * (number_of_floors - floor)
		pyramid_floors.append(space_number + (character * char_number) + space_number)
		char_number += 2
	return pyramid_floors
	

def main():
	#1 and #2. Handling errors and Parsing
	character, number_of_floors = parse_arguments()
	
	# 3. Resolution
	pyramid = create_floors_list(character, number_of_floors)
	
	# 4. Display
	print(*pyramid, sep="\n")

if __name__ == "__main__":
	main()