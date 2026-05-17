# Find Remainder Without Using Modulus Operator

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

remainder = first_number - (first_number // second_number) * second_number

print("Remainder =", remainder)