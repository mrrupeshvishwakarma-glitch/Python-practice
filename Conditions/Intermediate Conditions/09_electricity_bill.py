unit = int(input("Enter the unit : = ")) 
if unit <= 100:
    price = unit * 5
    print("Final amount: = ", price)
elif 100 <= unit <= 200: 
    price = unit * 8
    print("Total price: =", price)
else:
    price = unit * 10
    print("Total price: = ", price)
