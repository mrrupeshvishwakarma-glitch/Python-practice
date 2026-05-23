# Take salary and experience and classify promotion eligibility.

salary = int(input("Enter your salary: = "))
experience = int(input("Enter your experience (years): = "))

if salary >= 50000 and experience >= 5:
    print("Eligible for promotion")
else:
    print("Not eligible for promotion")