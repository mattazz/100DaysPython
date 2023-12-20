# Get the highest number

student_scores = [78, 65, 99, 22, 58, 92, 18, 90, 95]

print(max(student_scores))

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score

print(high_score)
