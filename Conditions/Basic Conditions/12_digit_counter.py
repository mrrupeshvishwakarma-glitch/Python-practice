num = int(input("Enter the number: = "))
if 0 <= num <= 9:
    print("1-Digit number")
elif 10 <= num <= 99:
    print("2-Digits number")
elif 100 <= num <= 999:
    print("3-Digits number")
else:
    print("More than 3-Digits")
