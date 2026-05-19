# Convert Total Seconds into Minutes and Seconds

total_seconds = int(input("Enter total seconds: "))

minutes = total_seconds // 60
seconds = total_seconds % 60

print("Minutes =", minutes)
print("Seconds =", seconds)