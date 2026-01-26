students = []
scores = []

for student in range(5):
    name = input("Enter your name: ")
    students.append(name)
    score = int(input("Enter your score: "))
    scores.append(score)
highest_score = max(scores)
position = scores.index(highest_score)
top_student = students[position]
average = sum(scores) / len(scores)

print(f"The student with the top score is {top_student}")
print(f"The class average is {average}")