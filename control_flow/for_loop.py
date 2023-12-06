"""
For Loop in Python
Iterable items are Strings, List, Tuple, Dictionary
"""
my_string = 'abcabcabc'
for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')
print("\n")
print("*" * 20)
cars = ["bmw", "honda", "audi"]
for car in cars:
    print(car)

print("*" * 20)
nums = [1, 2, 3]
for num in nums:
    print(num * 10)

print("*" * 20)
dic = {"one": 1, "two": 2, "three": 3}
for k in dic:
    print(k + " - " + str(dic[k]))

print("*" * 20)
for k, v in dic.items():
    print(str(k) + " : " + str(v))
