# Author CL 2/14/2021

user_input = input("What file do you want to count?\n")

with open(user_input, "r") as infile:
    lines = 0
    content = infile.readlines()
    for line in content:
        lines += 1

print("There are {0} lines in {1}".format(lines, user_input))