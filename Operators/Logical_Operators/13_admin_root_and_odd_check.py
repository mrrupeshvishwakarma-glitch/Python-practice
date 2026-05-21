# Take username and check if username == "admin" or username == "root".
username = input("Enter the Username : = ")
if username == "admin" or username == "root":
    print("Access granted")
else:
    print("Access denied")

# Take number and check if it is odd and greater than 50. 
num = int(input("Enter the number : = "))
if num % 2 != 0 and num > 50:
    print("Number is odd and greater than 50")
else:
    print("Condition not matched")
