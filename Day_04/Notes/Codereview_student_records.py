"""docstring"""

student_names=("Juan","Maria","Joseph")
student_scores = (70,90,81)
high_score = 0
high_score_student =""


def get_highest_score():
    """docstring"""
    student_records = zip(student_names, student_scores)
    for index, (name, score) in enumerate(student_records, start=1):

        if score > high_score:
            high_score = score
            high_score_student = name

        print(f"Student {index} {name} scored {score} in the exam." )

print(f"highscore: {high_score_student} ", high_score)