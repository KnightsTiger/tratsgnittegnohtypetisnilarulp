#if statement
x =10
if x>0:
    print(x)
else:
    print(x-1)

#elif

y=5
if y>10:
    print(y)
elif y>=5:
    print(y-1)
else:
    print("nooo")

boolval = False
#    not key word
if   not boolval:
    print (y)

# and key word

if x<10 and y>10:
    print(x)

# or keyword
if x>10 or y<5:
    print(y)

#Ternary if condition
a =1
b=3
print("grate") if b>a else print("less")