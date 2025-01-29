# 1 Example : Read & Access keys:
import json
file=open("my_json1.json","r")
x=file.read()
data = json.loads(x)  # Parse the JSON string into a dictionary
print()

# 2 example:
import json
f=open("student.json","r")
data=json.load(f)
print(data.get("id"))

# 3 Example:
import json
file = open("my_json1.json", "r")
# x = file.read()
data = json.load(file)  # Parse the JSON string into a dictionary
print(data.get("fruit"))  # Access the "fruit" key
file.close()


# 4 Example:
import json
data="student.json"
with open(data, "r") as file:
    x=json.load(file)
print(x.get("id")) # Access ID from student.
print(x)

#-------------------------------------------------------------------------------------

# 5 Example for Write json: like json.dump

import json
data={
    "name":"Irfan","roll":32,"add":"BKC"
}
with open("data.json","w") as f:
    json.dump(data,f)

#---------------------------------------------------------------------------------------

##Code to Fill Data in the JSON File:

import json

# JSON file path
data_file = "student.json"

# Data to be written
data = {
    "id": 1,
    "name": "John",
    "age": 21
}

# Write the data to the JSON file
with open(data_file, "w") as file:
    json.dump(data, file, indent=4)  # Pretty formatting with indent=4

print("Data has been written to the JSON file.") #Optional


## Append Data to an Existing JSON File: (Practice Remain) !!!

import json

file = "student.json"

# Step 1: Read the existing data from the file
try:
    with open(file, "r") as f:
        data = json.load(f)  # Read JSON data from the file
except (FileNotFoundError, json.JSONDecodeError):
    data = []  # If file doesn't exist or has invalid JSON, start with an empty list

# Step 2: If the data is a dictionary, turn it into a list
if isinstance(data, dict):
    data = [data]

# Step 3: Append new data
data.append({"name": "Amir", "age": 22})

# Step 4: Write the updated data back to the file
with open(file, "w") as newfile:
    json.dump(data, newfile, indent=4)

print()
