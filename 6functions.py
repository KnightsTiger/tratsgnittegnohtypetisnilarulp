#named arguments
students=[]
def studentDetails(name,age):
    std = {"name":name,"age":age}
    students.append(std)

studentDetails(name="kasun",age=33) # This is the place the arguments gettting a name
#print(students).

##--------------------------------------------------------------------------------------------##

# args
# we are using this to specify unlimited of arguments
# following is an example

def argsexample(name,*args): # In there there is a * in the args. 
    print(name) # this will print the name i.e. the first arugument value
    print(args) # This will print the rest of the values in the argument

##argsexample("saman",22,True,"colombo",3.1)

##--------------------------------------------------------------------------------------------##

# key word arguments
# in the above example we do not have a method to access to a specific value. eg:- we can't access to colombo value directly
# To solve this problem we can use "Keyword arguments"

def kwargsexample(name,**kwargs): # In there there is a ** in the args. 
    print(name) # this will print the name i.e. the first arugument value
    print(kwargs["age"]) # This will print the value of key word "age"

kwargsexample("saman",age=22,married=True,lives="colombo",height=3.1) # in here age is passed as 22 so the system will show that

##--------------------------------------------------------------------------------------------##

# Nested functions . THis is called as a closure
# These are functions within a function
# This allows more interoperability between a nested and an outer function