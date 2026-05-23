age = int(input("Enter your age: = "))
gender = input("Enter your gender (male/female): = ").lower()

if gender == "female" and (age <= 12 or age >= 60):
    print("Eligible for special ticket discount")
else:
    print("Not eligible")