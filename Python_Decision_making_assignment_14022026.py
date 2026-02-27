#Write a simple Python program to evaluate a student's result using conditional statements.

# Input student details
name = input("Enter Student Name: ")

maths = float(input("Enter Marks in Maths: "))
science = float(input("Enter Marks in Science: "))
english = float(input("Enter Marks in English: "))

# Validate marks
if (maths < 0 or maths > 100 or
    science < 0 or science > 100 or
    english < 0 or english > 100):
    print("Invalid marks entered")
    exit()
# Calculate total and average
total = maths + science + english
average = total / 3

# Determine Pass / Fail
if maths < 40 or science < 40 or english < 40:
    status = "Fail"
else:
    status = "Pass"
    
# Display results
print("\n--- Student Result ---")
print("Student Name:", name)
print("Total Marks:", total)
print(f"Average Percentage: {average:.2f}%")
print("Status:", status)

# Assign grade only if passed
if status == "Pass":
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    else:
        grade = "C"
    print("Grade:", grade)
    
    
    
    ##OUTPUT##########
    
    Enter Student Name: Karl
    Enter Marks in Maths: 76
    Enter Marks in Science: 38
    Enter Marks in English: 98

    --- Student Result ---
    Student Name: Karl
    Total Marks: 212.0
    Average Percentage: 70.67%
    Status: Fail 
    
    Enter Student Name: Karl
    Enter Marks in Maths: 76
    Enter Marks in Science: 38
    Enter Marks in English: 98

    --- Student Result ---
    Student Name: Karl
    Total Marks: 212.0
    Average Percentage: 70.67%
    Status: Fail