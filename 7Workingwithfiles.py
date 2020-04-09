####
#### This is not working
####



students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append( student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_Student(name,student_id=0):
    student = {"name":name,"student_id":student_id}
    students.append(student)

def savetofile(student):
    try:
        f = open("studnets.txt","a")# in here a file is creted and "a" means we want to append some text to this file
        f.write(student+"\n")
        f.close()
    except Exception:
        print("Could not save the file")

def readFile():
    try:
        f=open("students.txt","r")
        for student in f.readlines():
            add_Student(student)
        f.close()
    except Exception:
        print("Could not read file")

readFile()
print_students_titlecase()

student_name = input("Enter studnet Name :")
student_id = input("Enter student ID : ")

add_Student(student_name,student_id)
savetofile(student_name)

