this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)

print(len(this_dict))

#  Accessing a dictionary
x = this_dict["model"]
print(x)

y = this_dict.get("model")
print(y)

allKeys = this_dict.keys()  # Returns all the keys
print(allKeys)

allValues = this_dict.values()
print(allValues)  # Returns all the values

allItems = this_dict.items()  # Returns all the items of the dictionary
print(allItems)

if "model" in this_dict:
    print("Yes, 'model' is one of the keys in the this_dict dictionary")

#  Change values
this_dict["year"] = 2018
print(this_dict)

this_dict.update({"year": 2020})
print(this_dict)

#  Adding new items
this_dict["color"] = "red"
print(this_dict)

this_dict.update({"country": "USA"})
print(this_dict)

#  Removing items
this_dict.pop("model")
print(this_dict)

del this_dict["brand"]
print(this_dict)

this_dict.popitem()  # Removes the last inserted items
print(this_dict)

print()

#  Looping through a dictionary
for x in this_dict.keys():  # Return the keys
    print(x)

print()

for x in this_dict.values():  # Return the values
    print(x)

print()

for x, y in this_dict.items():  # Return all the items
    print(x, y)

print()

#  Copying a dictionary
myDict = this_dict.copy()
print(myDict)

anotherDict = dict(this_dict)
print(anotherDict)

#  Nested dictionary
myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myFamily)

print()

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(family)

print()

print(myFamily["child2"]["name"])
