"""
Identifies the number if odd or even
"""
int_number = int(input("Enter a number: "))

if (int_number % 2) == 0:
    print(f"Number {int_number} is even.")
else:
    print(f"Number {int_number} is odd.")
