
students_A = int(input("Enter Classroom A: "))
students_B = int(input("Enter Classroom B: "))
students_C = int(input("Enter Classroom C: "))
desks_A = students_A // 2 + (students_A % 2)
desks_B = students_B // 2 + (students_B % 2)
desks_C = students_C // 2 + (students_C % 2)
total_desks = desks_A + desks_B + desks_C
print(total_desks)
