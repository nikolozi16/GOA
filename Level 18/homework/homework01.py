# გაკვეთილების ცხრილი
grades = {
    'math': 85,
    'science': 90,
    'history': 78,
    'literature': 92
}

# საშუალო ქულის გამოთვლა
average_grade = sum(grades.values()) / len(grades)

# შედეგის დაბეჭვდა
print("Subject grades:", grades)
print(f"The average grade is {average_grade:.2f}")
