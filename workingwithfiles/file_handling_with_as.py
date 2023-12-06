"""
File handling 'with' and 'as'
"""
# print("Normal Write Start")
# my_write = open("textfile.txt", "w")
# my_write.write("Trying to write the file")
# my_write.close()
#
# print("Normal Read Start")
# my_read = open("textfile.txt", "r")
# print(str(my_read.read()))
# my_read.close()


print("With As Write Start")
with open("withas.txt", "w") as with_as_write:
    list_items = ["Hello\n", "World\n", "Python\n", "Program\n"]
    with_as_write.writelines(list_items)

print()
print("With As Read Start")
with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))

