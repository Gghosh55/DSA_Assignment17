def count_students(students, sandwiches):
    count = 0
    n = len(students)

    while students:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            count = 0
        else:
            students.append(students.pop(0))
            count += 1


        if count == n:
            break

    return len(students)
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(count_students(students, sandwiches))

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(count_students(students, sandwiches))
