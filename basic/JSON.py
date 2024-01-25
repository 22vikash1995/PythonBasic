import json

# json
student = '{"name":"Vikash kumar","age":26,"phone":"8810271698"}'
# parse the json using  load methods
x = json.loads(student)
print("name is:", x["name"], "\n age is:", x["age"])

# converting the python dictionary to json object
mydict = {"name": "Vicky", "email": "vicky@gmail.com", "phone": "881021698"}
print(mydict)
# convert it to json
jsonDict=json.dumps(mydict,indent=4)
print(jsonDict)
