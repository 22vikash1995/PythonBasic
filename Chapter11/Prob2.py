"""
Create a list of cricketers .Use this list to create a dictionary in which the list values becomes
keys of dictionary. Set the values of all keys to 50 in the dictionary created.
"""
# Creating a list of cricketers
cricketers = ['Rahul', 'Roshan', 'Gambhir', 'Bumrah', 'Sachin', 'Dhoni', 'Kohli', 'Jadeja']
# creating a dictionary which have keys as list items and setting the value 50 corresponding to each keys
cricket_dict=dict.fromkeys(cricketers,50)
print(cricket_dict)
print(cricketers)
