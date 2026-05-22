amount = int(input("Enter the amount: = "))
if amount > 5000:
    print("Eligible For Discount")
    print("Enter mode of payment")
    mode = input("A-Cash B-Card C-Upi: ")
    if mode == "B":
        print("Discount Applied ")
    elif mode == "A" or mode == "C":
        print("Discount not applied")
    else:
        print("In-Valid input")
elif (amount > 0) and (amount <= 5000):
    print("Not eligible ")
else:
    print("Please do shopping")
