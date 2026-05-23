# 1. Take a number and print:
#  - "Fizz" if divisible by 3
#  - "Buzz" if divisible by 5
#  - "FizzBuzz" if divisible by both
# otherwise print number

number = int(input("Enter the number: = "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
