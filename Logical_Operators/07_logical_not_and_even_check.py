# Take age and check if not (age < 18).
age = int(input("Enter your age: "))
if not age < 18:
    print("You are an adult")
else:
    print("You are a minor (under 18)")

# Take a number and check if it is even and greater than 10.
num = int(input("Enter the number: "))
if num % 2 == 0 and num > 10:
    print("Number is even and greater than 10")
else:
    print("Condition not matched")
