# Take password and check if it is not "1234". 
password = int(input("Enter the password : = "))
if password != 1234:
    print("Wrong password")
else:
    print("Correct password")

# Take two numbers and check if both are not equal to zero. 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 != 0 and num2 != 0:
    print("Both numbers are not equal to zero")
else:
    print("At least one number is zero")
