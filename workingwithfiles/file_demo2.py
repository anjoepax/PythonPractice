"""
Reading Files in Python
"""

my_file = open("firstfile.txt", 'r')
print(str(my_file.read()))
my_file.close()

print("Line by line =====>>>")

my_file_line = open("firstfile.txt", 'r')
my_lines = my_file_line.readlines()
for line in my_lines:
    print(line)
my_file_line.close()

