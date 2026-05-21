# Take age and check if age < 18 or age > 60.
age = int(input("Enter your age: "))
if age < 18 or age > 60:
    print("Person is under 18 or over 60")
else:
    print("Person is between 18 and 60")

# Take marks and check if marks < 35 or marks > 100.
marks = int(input('Enter your marks : = '))
if marks < 35 or marks > 100:
    print("Invalid or failing: marks are below 35 or above 100")
else:
    print("Valid passing marks")
