# Take two inputs and check if both are same and greater than 10. 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 == num2 and num1 > 10:
    print("Both numbers are same and greater than 10")
else:
    print("Condition not matched")

# Take number and check if it is not between 10 and 20. 
number = int(input("Enter the number : =  "))
if not (number >= 10 and number <= 20):
    print("Number is not between 10 and 20")
else:
    print("Number is between 10 and 20")
