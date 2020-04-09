#As a convention a class is starting from a capital letter
class Studnets:
    print("done")

##saman = Studnets()

#--------------------------------------------------------------------#

#Adding a method to a class
# calsses = []

# class NewStudents:
#     def addClass(self,name,count): #Without self keyword this will not work
#         newClass = {"name":name,"Count":count}
#         calsses.append(newClass)
# student = NewStudents()
# student.addClass("Java",10)
# print(calsses)

#--------------------------------------------------------------------#

#Adding constructor

# calsses = []

# class NewStudents:
#     def __init__(self,name,count): #Without self keyword this will not work
#         newClass = {"name":name,"Count":count}
#         calsses.append(newClass)
# student = NewStudents("Java",10)

#--------------------------------------------------------------------#

#overriding str method
# calsses = []

# class NewStudents:
#     def __init__(self,name,count): #Without self keyword this will not work
#         newClass = {"name":name,"Count":count}
#         calsses.append(newClass)
#     def __str__(self):
#         return "Students class"
# student = NewStudents("Java",10)
# print(student) # here you can find the overrided variable

#--------------------------------------------------------------------#

# class JavaClass:
#     courseName =  "Java" #This is a class attribute. So from outside this can access

#     def setCount(self,numberOfStudents):
#         self.numberOfStudents = numberOfStudents # numberOfStudents can access from anywhere in the program
    
#     def getCount(self):
#         return self.numberOfStudents
    
# print(JavaClass.courseName) 

# myClass = JavaClass()
# myClass.setCount(10)
# print(myClass.getCount())

#--------------------------------------------------------------------#

# Inheritance

class JavaClass:
    courseName =  "Java" #This is a class attribute. So from outside this can access

    def setCount(self,numberOfStudents):
        self.numberOfStudents = numberOfStudents # numberOfStudents can access from anywhere in the program
    
    def getCount(self):
        print("hi")
    
class courses(JavaClass):
    courseName = "Advance"

    def __str__(self):
        return "Super Class"

print(JavaClass.courseName) 

myClass = JavaClass()
myClass.setCount(10)
print(myClass.getCount())


myClassMain = courses()
print(myClassMain.courseName)
print(myClassMain.getCount())
print(myClassMain)  