Text = input("Enter the string: = ")
length = len(Text)
if length < 5:
    print("Short")
elif 5 <= length <= 10:
    print("Medium")
else:
    print("Long")
