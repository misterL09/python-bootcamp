student_names =("Juan","Maria","Joseph")
student_scores = (70,90,81)
high_score = 0
high_score_student =""

for index, (var1,var2) in enumerate(zip(student_names,student_scores),start = 1):
    if var2 > high_score:
        high_score = var2
        high_score_student = var1

    print(f"Student {index} {var1} scored {var2} in the exam." )

print(f"highscore: {high_score_student} ", high_score)