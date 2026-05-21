# Take number and check if it is not zero.
num = int(input("Enter the number: "))
if num != 0:
    print("The number is not zero")
else:
    print("The number is zero")

# Legally age calculation:
age = int(input("Enter your age : = "))
if age >= 18 and age <= 60:
    print("You are an adult (18 to 60)")
elif age < 18:
    print("You are a minor (Under 18)")
else:
    print("You are a senior citizen person (Above 60)")
