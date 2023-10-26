#!/usr/bin/env python3

# Exercise 11. Afficher le contenu / Display a file content 
 
import argparse

def is_file(file_name):
	try: 
		return open(file_name, "r")
	except FileNotFoundError:
		print("error")
		exit()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a file name.")
    parser.add_argument('file_name', help='A list of values of any type')
    args = parser.parse_args()
    return args.file_name

def read_file_name(file_name):
	file = open(file_name, "r")
	return file.read()

def main():
	#1 and #2. Handling errors and Parsing
	file_name = parse_arguments()
	is_file(file_name)

	# 3. Resolution
	file_content = read_file_name(file_name)
	
	# 4. Display
	print(file_content)

if __name__ == "__main__":
	main()
