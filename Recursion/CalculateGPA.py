# Calculating GPA

print("""Welcome to the GPA calculator!
Please enter the grade by letters:
Enter a blank after you entered your grades to calculate the GPA""")


points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67,
          'D+': 1.33, 'D': 1.0, 'F': 0.0}

num_courses = 0
total_num = 0
grades = []
while True:
    grade = input()

    if grade == '':
        break
    elif grade not in points:
        print("Grade is not in letter format. Please enter the grade correctly!")
    else:
        num_courses += 1
        total_num += points[grade]
        grades.append(grade)

if num_courses > 0:
    GPA = total_num / num_courses
    print(f"The number of courses: {num_courses}")
    print(f"Your GPA is:{GPA}")

print(f" grades are : {grades}")


def count(data, target):
    for item in data:
        if item == target:
            return True
        return False


prize = count(grades, 'A')
print(f"Do you have at least one 'A' in your grades? {prize}")
