student_scores = [98,75,100,86,100,3]

lowest_score = min(student_scores)
print(lowest_score)

highest_score = max(student_scores)
print(highest_score)

print(sum(student_scores))

print("Average Score: ",sum(student_scores)/len(student_scores))

print(sorted(student_scores,reverse=True))
print(*sorted(student_scores,reverse=True))