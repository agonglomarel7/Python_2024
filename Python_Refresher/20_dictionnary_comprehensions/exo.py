# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    "name": "Jose",
    "school": "Computing",
    "grades":(66,77,88)
}

print(student["grades"])

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =  data["grades"]
    return sum(grades) / len(grades)

print(average_grade({
    "name": "Jose",
    "school": "Computing",
    "grades":(66,77,88)
}))

student_list=[
    {
    "name": "Jose",
    "school": "Computing",
    "grades":(66,77,88)
},
{
    "name": "Jose",
    "school": "Computing",
    "grades":(66,77,88)
},    {
    "name": "Jose",
    "school": "Computing",
    "grades":(66,77,88)
}
]

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])
    return total / count if count > 0 else 0

print(average_grade_all_students(student_list))