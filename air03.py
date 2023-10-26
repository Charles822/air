#!/usr/bin/env python3

# Exercise 4. Chercher l'intrus / Find the intruder
 
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process an arbitrary number of arguments.')
	parser.add_argument('arguments', nargs='+', help='Input arguments.')
	args = parser.parse_args()
	return args.arguments

"""      
def find_the_intruder(arguments): # find the intruder using the built in function count
	for element in arguments: 
		if arguments.count(element) != 2:
			return element
	else:
		return "error"
"""

def find_the_intruder(arguments):
    count_dict = {}
    for argument in arguments:
        if argument in count_dict:
            count_dict[argument] += 1
        else:
            count_dict[argument] = 1

    for argument, count in count_dict.items():
        if count != 2:
            return argument

    return "error"

				
def main():
	#1 and #2. Handling errors and Parsing
	arguments = parse_arguments()

	# 3. Resolution
	intruder = find_the_intruder(arguments)
	
	# 4. Display
	print(intruder)

if __name__ == "__main__":
	main()
