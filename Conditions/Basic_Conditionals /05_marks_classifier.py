marks = int(input("Enter the marks: =  "))
if marks < 35:
    print("fail")
elif marks >= 35 and marks <= 59:
    print("Pass")
elif marks >= 60 and marks <= 79:
    print("First division")
else:
    print("Distinction")
