# Take temperature and check if temp > 40 or temp < 0.
temp = int(input("Enter the temperature : = "))
if temp > 40 or temp < 0:
    print("Extreme weather: too hot or freezing")
else: 
    print("Temperature is in normal range")

# Take two numbers and check if at least one is negative.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 < 0 or num2 < 0:
    print("At least one is negative")
else: 
    print("Both are positive")
