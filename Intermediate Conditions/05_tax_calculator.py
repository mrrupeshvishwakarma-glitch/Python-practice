income = int(input("Enter the income: = "))
if income <= 250000:
    print("No tax")
elif 250000 <= income <= 500000:
    tax = (income * 5)/100
    print("Tax", tax)
    print("Final income: = ", income - tax)
elif 500000 <= income <= 1000000:
    tax = (income * 10)/100
    print("Tax", tax)
    print("Final income: = ", income - tax)
else:
    tax = (income * 20)/100
    print("Tax", tax)
    print("Final income: = ", income - tax)
