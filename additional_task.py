grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_assessment = dict()

yongling1 = float(sum(grades[0]) / len(grades[0]))
yongling2 = float(sum(grades[1]) / len(grades[1]))
yongling3 = float(sum(grades[2]) / len(grades[2]))
yongling4 = float(sum(grades[3]) / len(grades[3]))
yongling5 = float(sum(grades[4]) / len(grades[4]))

sort_students = sorted(students)
student_assessment.update(({sort_students[0]: yongling1, sort_students[1]: yongling2, sort_students[2]: yongling3,
                            sort_students[3]: yongling4, sort_students[4]: yongling5}))
print(student_assessment)