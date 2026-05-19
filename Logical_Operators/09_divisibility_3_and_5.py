# Take number and check if it is divisible by 3 and 5.
number = int(input("Enter the number: = "))
if number % 3 == 0 and number % 5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")

# Take number and check if it is divisible by 3 or 5.
num = int(input("Enter the number: = "))
if num % 3 == 0 or num % 5 == 0:
    print("Number is divisible by 3 or 5")
else:
    print("Number is not divisible by 3 or 5")
