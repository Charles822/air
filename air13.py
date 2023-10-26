#!/usr/bin/env python3

# Exercise 14. Meta exercise

import subprocess


class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    

def is_file_exist(air_files):
	for file in air_files:
		try: 
			open(file, "r")
		except FileNotFoundError:
			print(f"error, {file} is not in this directory")
			exit()


def run_test(results_test, script_name, test_args, expected_results):
    for i, (args, expected) in enumerate(zip(test_args, expected_results), 1):
        # Using the * operator to unpack the arguments from the tuple
        result = subprocess.run(["python3", f"./{script_name}.py", *args], capture_output=True, text=True).stdout.strip()
        if result == expected:
            results_test.append(f"{script_name} {i}/{len(test_args)}) : success")
        else:
            results_test.append(f"{script_name} {i}/{len(test_args)}) : failure")
    return results_test

def success_count(results_test):
	success = 0
	for test in results_test:
		if "success" in test:
			success += 1
	return success


def add_color(results_test, colored_tests_results):
	for item in results_test:
		if "success" in item:
			colored_tests_results.append(item.replace("success", f"{bcolors.OKGREEN}success{bcolors.ENDC}"))
		elif "failure" in item:
			colored_tests_results.append(item.replace("failure", f"{bcolors.FAIL}failure{bcolors.ENDC}"))
	return colored_tests_results


def main():
	#1 Handling errors 
	air_files = ["./air00.py", "./air01.py", "./air02.py", "./air03.py", "./air04.py", "./air05.py", "./air06.py", \
	"./air07.py", "./air08.py", "./air09.py", "./air10.py", "./air11.py", "./air12.py", "./air14.py"]
	is_file_exist(air_files)
	
	#2 Parsing
	results_test = []
	colored_tests_results = []
	
	# 3. Resolution
	run_test(results_test, "air00", [("Bonjour les gars",), ("bonjour",), ("Bonjour les gars",)], ["Bonjour\nles\ngars", "error", "salut"])
	run_test(results_test, "air01", [("Crevette magique dans la mer des étoiles", "la"), ("Crevette magique dans la mer des étoiles", "des")], \
		["Crevette magique dans \n mer des étoiles", "Crevette magique dans la mer \n étoiles"])
	run_test(results_test, "air02", [("je", "teste", "des", "trucs", " ")], ["je teste des trucs"])
	run_test(results_test, "air03", [("1", "2", "3", "4", "5", "4", "3", "2", "1")], ["5"])
	run_test(results_test, "air04", [("Hello milady,   bien ou quoi ??",)], ["Helo milady, bien ou quoi ?"])
	run_test(results_test, "air05", [("1", "2", "3", "4", "5", "+2")], ["3 4 5 6 7"])
	run_test(results_test, "air06", [("Michel", "Albert", "Thérèse", "Benoit", "t")], ["Michel"])
	run_test(results_test, "air07", [("1", "3", "4", "2")], ["1 2 3 4"])
	run_test(results_test, "air08", [("10", "20", "30", "fusion", "15", "25", "35")], ["10 15 20 25 30 35"])
	run_test(results_test, "air09", [("Michel", "Albert", "Thérèse", "Benoit")], ["Albert, Thérèse, Benoit, Michel"])
	run_test(results_test, "air10", [("a.txt",)], ["Je danse le mia"])
	run_test(results_test, "air11", [("o", "5")], ["    o    \n   ooo   \n  ooooo  \n ooooooo \nooooooooo"])
	run_test(results_test, "air12", [("6", "5", "4", "3", "2", "1")], ["1 2 3 4 5 6"])
	
	success_display = f"Total success: ({success_count(results_test)}/{len(results_test)})"
	add_color(results_test, colored_tests_results)

	# 4. Display
	print(*colored_tests_results, sep="\n")
	print(f"...\n{success_display}")

if __name__ == "__main__":
	main()




