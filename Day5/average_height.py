# Average height exercise

student_heights = [180, 124, 165, 173, 189, 169, 146]


def loop_ave():
    ave = 0
    for i in student_heights:
        ave += i

    res = ave / len(student_heights)
    res = round(res, 2)
    print(f"The average student height is {res}")


def other_answer():
    res = sum(student_heights) / len(student_heights)
    res = round(res, 2)
    print(f"Alternative answer: {res}")


loop_ave()
other_answer()
