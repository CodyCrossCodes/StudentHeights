student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
number_of_students = 0

for average_height in student_heights:
    total_height += average_height
    number_of_students += 1

average = round(total_height / number_of_students)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average}")