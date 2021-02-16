# Author CL 2/14/2021

user_input = input("What file do you want to count?\n")

with open(user_input, "r") as infile:
    lines = []
    content = infile.readlines()
    for line in content:
        if len(line) == 0:
            del line
        len_line = len(line)
        lines.append([line, len_line])
    lines.sort()

print("The longest line is: ")
print(lines[0]), print("characters long")
