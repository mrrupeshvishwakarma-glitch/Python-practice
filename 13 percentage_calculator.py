# Percentage Calculator

hindi_marks = int(input("Enter Hindi marks: "))
english_marks = int(input("Enter English marks: "))
accountancy_marks = int(input("Enter Accountancy marks: "))
business_studies_marks = int(input("Enter Business Studies marks: "))
information_technology_marks = int(input("Enter Information Technology marks: "))

total_marks = (
    hindi_marks
    + english_marks
    + accountancy_marks
    + business_studies_marks
    + information_technology_marks
)

percentage = total_marks / 5

print("Total Percentage =", percentage)