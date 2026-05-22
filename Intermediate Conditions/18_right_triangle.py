h = float(input("Enter the hypotenuse: = "))
p = float(input("Enter the perpendicular: = "))
b = float(input("Enter the base: = "))

if h**2 == p**2 + b**2:
    print("It is a right triangle")
else:
    print("It is not a right triangle")
