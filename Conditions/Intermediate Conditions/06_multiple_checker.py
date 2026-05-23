num1 = int(input("Enter the first number: = "))
num2 = int(input("Enter the second number: = "))
if num1 % num2 == 0:
    print(f"{num1} is multiple of {num2} ")
elif num2  % num1 == 0:
    print(f"{num2} is multiple of {num1}")
else:
    print("Neither number is multiple of another ")
