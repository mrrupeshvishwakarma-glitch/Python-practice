attempts = 0

while attempts < 3:
    password = input("Enter password: = ")

    if password == "admin123":
        print("Login successful")
        break
    else:
        attempts += 1
        print("Wrong password")

if attempts == 3:
    print("Warning! Too many login attempts")