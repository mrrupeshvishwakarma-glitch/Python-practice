salary = int(input("Enter basic salary: = "))
experience = int(input("Enter your experience in years: = "))
if experience < 2:
    bonus = 0 
elif experience <= 5:
    bonus = (salary * 10)/100
else:
    bonus = (salary * 20)/100

total_salary = salary + bonus

print("Bonus: = ", bonus)
print("Total salary: = ", total_salary)
