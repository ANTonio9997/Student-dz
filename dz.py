from comand import Student

student1 = Student("Vasya", 2003, "Група 1", 4.5)
student2 = Student("Petya", 2002, "Група 2", 3.8)

print(student1)
print(f"Вік: {student1.get_age()}\n")

print(student2)
print(f"Вік: {student2.get_age()}\n")
