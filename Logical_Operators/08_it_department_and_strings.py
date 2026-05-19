# Take salary and check if salary > 50000 or department == "IT".
salary = float(input("Enter your salary: = "))
department = input("Enter your department: = ")
if salary > 50000 or department == "IT":
    print("Employee is eligible")
else:
    print("Condition not matched")

# Take two strings and check if both are equal and not empty. 
str1 = input("Enter first string: = ")
str2 = input("Enter second string: = ")
if str1 == str2 and str1 != "":
    print("Both strings are equal and not empty")
else: 
    print("Condition not matched")
