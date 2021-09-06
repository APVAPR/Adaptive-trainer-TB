def score(marks: list, simbol):
    marks_count = len(marks)
    result = round(marks.count(simbol) / marks_count, 2)
    if simbol not in marks:
        return f'0.00'
    return '{0:.2f}'.format(result)


marks = 'A', 'B', 'C', 'D', 'E', 'F'
marks_students = input().split()
marks_status = True
for i in marks_students:
    if i not in marks:
        marks_status = False
        break

if marks_status:
    print(score(marks_students, "A"))

