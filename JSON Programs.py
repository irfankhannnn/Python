# Example:  fav
import json
data="student.json"
with open(data, "r") as file:
    x=json.load(file)
print(x.get("id")) # Access ID from student.
print(x)


#---------------------------------------------------------------------------------------
# ## Append Data to an Existing JSON File:

import json

data_file = "student.json"

# Read existing data
with open(data_file, "r") as file:
    data = json.load(file)

# !!! If you use same key to replace replace automaticaly: !!!

# Add new data
data["new_key"] = {"new_value":"None","age":22},{"naam":"Dalla"}
  # Or
data["new_key1"] = "new_value","Add More"

# Write updated data back
with open(data_file, "w") as file:
    json.dump(data, file, indent=4)

print("Data added successfully!")

#-------------------------------------------------------------------------------
## Update exixting data:
import json

file_name = "student.json"

# Step 1: Read the JSON file
with open(file_name, "r") as f:
    data = json.load(f)  # Load JSON content into a dictionary

# Step 2: Modify the data
data["Ebarat"]["Phone"] = "123456789"

# Step 3: Write the updated data back to the file
with open(file_name, "w") as f:
    json.dump(data, f, indent=4)

print("Phone number updated successfully!")


#-------------------------------------------------------------------------------

## delete data from json file:

import json

# File path
data = "student.json"

# Step 1: Read the JSON file
with open(data, "r") as file:
    x = json.load(file)

# Step 2: Delete the "class" key if it exists
if "new_key1" in x:
    del x["new_key1"]

# Step 3: Write the updated JSON back to the file
with open(data, "w") as file:
    json.dump(x, file, indent=4)
    
print(json.dumps(x, indent=4))

#-----------------------------------------------------------------------------------------------
## Rename key of Json file:
import json

data = "student.json"

# Load JSON from file
with open(data, "r") as f:
    x = json.load(f)

# Rename the key in the "Mobile" list
for mobile in x.get("Mobile", []):  # Loop through the list
    if "naam" in mobile:
        mobile["name"] = mobile.pop("naam")  # Rename key

# Save the updated JSON back to the file
with open(data, "w") as f:
    json.dump(x, f, indent=4)

print("Key renamed successfully.")

##-------------------------------------------------------------------------------
## Rename key of key:
import json

data_file = "student.json"

# Load JSON from file
with open(data_file, "r") as f:
    data = json.load(f)

# Rename the key inside "Ebarat"
if "Ebarat" in data and "age" in data["Ebarat"]:
    data["Ebarat"]["YearsOld"] = data["Ebarat"].pop("age")  # Rename "age" to "YearsOld"

# Save the updated JSON back to the file
with open(data_file, "w") as f:
    json.dump(data, f, indent=4)

print("Key renamed successfully.")




#================================ Complex JSON ================================

import json
data="jsoncomplex.json"
with open (data,"r") as f:
    x=json.load(f)
# Accesing Data:
print(x["accounting"][0]["lastName"])
print(x["accounting"][0]["firstName"]) # Accessing firstname from accounting.
print(x["sales"][0]["firstName"]) # Accessing firstname from sales.
# Loop through all employees in sales
for employee in x ["sales"]:
    print(employee["firstName"], employee["age"])

# Access only Sales:
for emp in x ["sales"]: # Ex 1
    print(emp)

print(x["sales"])       # Ex 2


## Insert Data (Remain) !!!
