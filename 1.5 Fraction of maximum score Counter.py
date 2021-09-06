from collections import Counter

marks_student = input().split()

a = Counter(marks_student)
print('{:.2f}'.format(a['A'] / len(marks_student)))
