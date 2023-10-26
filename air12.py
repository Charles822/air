#!/usr/bin/env python3

# Exercise 13. le roi des tri / Quicksort
 
import argparse
from math import floor

def is_int(value):
	try:
		return int(value)
	except ValueError:
		raise argparse.ArgumentTypeError("Your second argument must be an integer.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a list of intergers.")
    parser.add_argument('array_to_sort', nargs='+', type=is_int, help='Any int')
    args = parser.parse_args()
    return args.array_to_sort


def partition(array_to_sort, lo, hi):
	pivot = array_to_sort[floor((hi - lo)/2) + lo] # The value in the middle of the array
	return pivot


def quicksort(array_to_sort, lo, hi):
	if lo >= 0 and hi >= 0 and lo < hi:
		i = lo - 1 
		j = hi + 1
		a = 0 #to create an infinite loop
		while a == 0:
			while array_to_sort[i] < hi:
				i = i + 1 
			while array_to_sort[j] > hi:
				j = j - 1
			if i >= j:
				return j
			array_to_sort[i], array_to_sort[j] = array_to_sort[j], array_to_sort[i]
	return array_to_sort


def main():
	#1 and #2. Handling errors and Parsing
	array_to_sort = parse_arguments()
	lo = 0
	hi = len(array_to_sort) - 1
	p = partition(array_to_sort, lo, hi) 
	
	# 3. Resolution
	quicksort(array_to_sort, lo, p) # Note: the pivot is now included
	sorted_array = quicksort(array_to_sort, p + 1, hi)
	
	# 4. Display
	print(*sorted_array, sep=" ")

if __name__ == "__main__":
	main()
