students = []

def readNames():
    try:
        name=open("studnets.txt","r")
        for student in name.readlines():
            students.append(student)
        name.close()
    except Exception:
        print("Error occured")

readNames()
print(students)