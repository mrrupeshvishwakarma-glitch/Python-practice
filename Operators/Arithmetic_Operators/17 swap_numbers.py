# Swap Two Numbers Using Arithmetic Operators

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print("After swapping:")

print("First number =", first_number)
print("Second number =", second_number)