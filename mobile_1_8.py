grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в список для удобства работы
sorted_students = sorted(students)

# Создаем пустой словарь для хранения результатов
avg_grades = {}

for i in range(len(grades)):
    student = sorted_students[i]
    grade_list = grades[i]

    # Рассчитаем средний балл
    avg_grade = sum(grade_list) / len(grade_list)

    # Добавляем пару "ученик-средний балл" в словарь
    avg_grades[student] = round(avg_grade, 2)

# Выводим результаты
for student, avg_grade in avg_grades.items():
    print(f"{student}: {avg_grade}")
