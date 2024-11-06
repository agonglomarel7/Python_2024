

class Student:

    def __init__(self,name,grades):

        self.name = name
        self.grades = grades

    def average_grades(self):
        average = sum(self.grades) / len(self.grades)
        return f"The average {self.name} is {average}"

#declare an object of type Student

student  = Student("Bob", (100,100,20,89,45))

print(student.average_grades())