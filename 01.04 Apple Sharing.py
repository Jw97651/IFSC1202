students = int(input("Enter the number of students: "))
apples = int(input("Enter the number of apples: "))
apples_per_student = apples // students
apples_remaining = apples % students
print(f"Each student will get {apples_per_student} apples.")
print(f"There will be {apples_remaining} apples remaining in the basket.")
#remember, print f is used to format a string