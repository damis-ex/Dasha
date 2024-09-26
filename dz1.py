class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


student1 = Student("Іван", [5, 9, 7, 12, 10])
print(student1.average_grade())
