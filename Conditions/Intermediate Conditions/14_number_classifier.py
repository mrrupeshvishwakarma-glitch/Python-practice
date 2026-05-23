num = int(input("Enter the number: =  "))
if num == 0:
    print("Number is zero (even number)")
elif num % 2 == 0 and num > 0:
    print("Number is even and positive")
elif num % 2 == 0 and num < 0 :
    print("Number is even and negative")
elif num % 2 != 0 and num < 0:
    print("Number is odd and negative")
else:
    print("Number is odd and positive")
