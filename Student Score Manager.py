names = []
scores = []
passes = 0
fails = 0

# Input number of students
while True:
    num_of_students = int(input("Enter the number of students: "))
    if num_of_students < 0:
        print("Please enter a positive number")
    elif num_of_students == 0:
        print("No scores are available")
        break
    else: break

# Only continue if there is at least one student
if num_of_students > 0:
    # Input student names and scores
    for _ in range(num_of_students):
        name = input("Enter student name: ")
        names.append(name)
        score = int(input("Enter score (0-100): "))
        while not 0 <= score <= 100:
            score = int(input("Enter a valid score (0-100): "))
        scores.append(score)

    # Calculate highest, lowest, average
    highest = max(scores)
    lowest = min(scores)
    average = round(sum(scores) / len(scores), 2)

    # Count passes and fails
    for score in scores:
        if score >= 40:
            passes += 1
        else:
            fails += 1

    # Print each student with grade in the order entered
    print("\nStudent Scores and Grades:")
    for i in range(len(names)):
        score = scores[i]
        if 70 <= score <= 100:
            grade = "A"
        elif 60 <= score <= 69:
            grade = "B"
        elif 50 <= score <= 59:
            grade = "C"
        elif 40 <= score <= 49:
            grade = "D"
        else:
            grade = "F"
        print(f"{names[i]} - {score} - Grade: {grade}")

    # Print summary
    print(f"\nThe highest score is: {highest}")
    print(f"The lowest score is: {lowest}")
    print(f"The average score is: {average}")
    print(f"Exactly {passes} students passed")
    print(f"Exactly {fails} students failed")
