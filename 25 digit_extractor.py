# Extract Digits from a 3-Digit Number

number = int(input("Enter a 3-digit number: "))

last_digit = number % 10
middle_digit = (number // 10) % 10
first_digit = number // 100

print("First digit =", first_digit)
print("Middle digit =", middle_digit)
print("Last digit =", last_digit)