# Dictionaries are store key value paires
# Dictionaries are important once JSON values parsing

#An empty dictionary
dictionary1 = {}
#print(dictionary1)

dictionary2 = {
    "Name":"Saman",
    "Age":33
}
#printing the entire dictionary
#print(dictionary2)
# Pritinging a specific value
# print(dictionary2["Name"])
#note - if key is not given then there is an error

# getting all keys in a dictionary
#print(dictionary2.keys())

# Deleting a value
del dictionary2["Name"]
print(dictionary2)