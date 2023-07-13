student_scores = input("Input a list of student scores ").split()
highest_score=0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if highest_score<int(student_scores[n]):
      highest_score= student_scores[n]
print(student_scores)
print(f"The highest score in the class is: {highest_score}")

# Output

# Input a list of student scores  78 65 89 86 55 91 64 89
# [78, 65, 89, 86, 55, 91, 64, 89]
# The highest score in the class is: 91