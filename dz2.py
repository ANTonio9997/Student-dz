class Student:
    name = ''
    birth_year = 2000
    group = ''
    average_grade = 0.0

    def __init__(self, name, birth_year, group, average_grade):
        self.name = name
        self.birth_year = birth_year
        self.group = group
        self.average_grade = average_grade

    def __str__(self):
        return f"-- {self.name} --\nРік народження: {self.birth_year}\n" \
               f"Група: {self.group}\nСередній бал: {self.average_grade:.2f}"

    def get_age(self):
        current_year = datetime.date.today().year
        return current_year - self.birth_year

import datetime