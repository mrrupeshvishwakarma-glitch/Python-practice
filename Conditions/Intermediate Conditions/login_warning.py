attempts = int(input("Enter login attempts: = "))

if attempts >= 3:
    print("Warning! Too many login attempts")
else:
    print("Login allowed")