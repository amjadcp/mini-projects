#! /usr/bin/env python

"""
Author : Amjad
Date   : 16 May 2021
Description : This is my min_project1
"""

print("++++++++++++++++++++++++++++++")
print("++++ STUDENT GRADE FINDER ++++")
print("++++++++++++++++++++++++++++++")

limit = int(input("No.of students in list => "))
students = []
marks = []
grades = []
i = 0

while i<limit:
    print("-------------------" + str(i+1) + "-------------------\n")
    name = input("Name : ")
    mark = int(input("Mark :"))
    students.append(name)
    marks.append(mark)
    if mark>=40:
        grades.append("A")
    elif mark>=30:
        grades.append("B")
    elif mark>=20:
        grades.append("C")
    elif mark>=10:
        grades.append("D")
    else:
        grades.append("FAIL")
    i += 1

print("=================================")
print("======= GRADE LIST ==============")
print("=================================")

i = 0

while i<limit:
    print("-------------------" + str(i + 1) + "-------------------\n")
    print("NAME : " + students[i])
    print("MARK : " + str(marks[i]))
    print("GRADE : " + grades[i])
    i += 1

print("\n\n\n===============================================================================")
print("========================= MARK DOESN'T DECIDE YOUR FUTURE =======================")
print("===============================================================================")