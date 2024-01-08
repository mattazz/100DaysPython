student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

grades = {}

for k, v in student_scores.items():
    score = ""
    # Check grades
    if v <= 70:
        score = "Fail"
    elif v > 70 and v <= 80:
        score = "Acceptable"
    elif v > 80 and v <= 90:
        score = "Exceeds Expectations"
    else:
        score = "Outstanding"

    grades[k] = score

for k, v in grades.items():
    print(f"{k}: {v}")
