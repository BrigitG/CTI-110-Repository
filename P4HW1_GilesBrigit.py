# CTI-110
# P4HW1 - Score List
# Brigit Giles
# 4/3/2023

import string

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Program to store grades entered by the user and display various statistics\n")

# Ask user to enter number of scores to enter
num_scores = int(input("How many scores do you want to enter?: "))

# Create an empty list to store the grades
grades = []

# Loop to collect grades
for i in range(num_scores):
    valid_score = False
    while not valid_score:
        score = float(input(f"Enter score #{i+1}: "))
        if score >= 0 and score <= 100:
            valid_score = True
            grades.append(score)
        else:
            print("INVALID score entered!!!!"
                "\n Score must be between 0 and 100.")

# Find the lowest grade
lowest = min(grades)

# Remove the lowest grade from the list
grades.remove(lowest)

# Find the highest grade
highest = max(grades)

# Find the sum of grades
total = sum(grades)

# Find the average of grades
average = total / len(grades)

# Determine the letter grade for the calculated average
letter_grade = calculate_grade(average)

# Display the results
print("\n---------------Results---------------")
print("Lowest score: ",lowest)
print("Modified List:",grades)
print("Score Average: {:.2f}".format(average))
print("Grade:        ",letter_grade)
print("-------------------------------------")
