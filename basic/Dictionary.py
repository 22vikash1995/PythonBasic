dictionary = {
    "Name:": "Vkash kumar",
    "Father's Name:": "Narad Prasad",
    "Contact No.": "8810271698",
    "colors": ['red', 'white', 'blue']
}

print(dictionary)
# dictionary using dict() constructor
newDict = dict(name="Vikash", age=26, dob="19-06-1997")
print(newDict)
# access dictionary item
print(newDict["name"])
# access dictionary item by using get method
print(newDict.get("name"))

# getting all the keys present in dictionary
keys = newDict.keys()
print(keys)
# Add new item to dictionary
dictionary["email"] = "vikash@gmail.com"
print(dictionary["email"])
print(dictionary)
# print all values in the dictionary
print(dictionary.values())
# get dictionary items
print(dictionary.items())
# update dictionary item
dictionary.update({"email": "vikkyrajbth97@gmail.com"})
print(dictionary)
# remove item from dictionary
dictionary.pop("email")
print(dictionary)
# remove last inserted item
dictionary.popitem()
print(dictionary)
# loop in dictionary
for item in dictionary:
    print(item)
# print all values in dictionary
for i in dictionary:
    print(dictionary[i])
# print all items with keys and values
for x,y in dictionary.items():
    print(x,y)
