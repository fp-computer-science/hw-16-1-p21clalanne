# Author CL 2/14/2021

with open("alice.txt", "r") as infile:
    dictionary = {}
    for lines in infile:
        new_lines = lines.strip()
        lines_split = new_lines.split()
        for value in lines_split:
            if value in dictionary:
                dictionary[value] += 1
            if value not in dictionary:
                dictionary[value] = 1

dictionary_list = list(dictionary.items())
for value in dictionary_list:
    print(value)
