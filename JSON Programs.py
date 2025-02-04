# Key Points:
#Use json.dump() to write data to a file.
#Use json.load() to read JSON data from a file.v
#-------------------------------------------------------------------------------------------------
# # 1 Example : Read & Access keys:
# import json
# file=open("my_json1.json","r")
# x=file.read()
# data = json.loads(x)  # Parse the JSON string into a dictionary
# print()

#------------------------------------------------------------------------------------------------


# # 2 example:
# import json
# f=open("student.json","r")
# data=json.load(f)
# print(data.get("id"))

#----------------------------------------------------------------------------

# # 3 Example: 
# import json
# file = open("my_json1.json", "r")
# # x = file.read()
# data = json.load(file)  # Parse the JSON string into a dictionary
# print(data.get("fruit"))  # Access the "fruit" key
# file.close()

#------------------------------------------------------------------------------

# 4 Example:  fav
import json
data="student.json"
with open(data, "r") as file:
    x=json.load(file)
print(x.get("id")) # Access ID from student.
print(x)

#-------------------------------------------------------------------------

# Remove output Ebarat from student.json file: (Data Filtring)
# import json
# data_file="student.json"
# with open (data_file, "r") as f:
#     data=json.load(f)

# filtered_data = [person for person in data if person["name"] != "Ebarat"]
# print(filtered_data)

#-------------------------------------------------------------------------------------

# 5 Example for Write json: like json.dump

# import json
# data={
#     "name":"Irfan","roll":32,"add":"BKC"
# }
# with open("data.json","w") as f:
#     json.dump(data,f)

#---------------------------------------------------------------------------------------

# ##Add Data to an Existing JSON File:

import json

data_file = "student.json"

# Read existing data
with open(data_file, "r") as file:
    data = json.load(file)

# !!! If you use same key to replace replace automaticaly: !!!

# Add new data
data["new_key"] = {"new_value":"None","age":22},{"naam":"Dalla"} # Replace
  # Or
data["new_key1"] = "new_value","Add More"

# Write updated data back
with open(data_file, "w") as file:
    json.dump(data, file, indent=4)

print("Data added successfully!")

#-------------------------------------------------------------------------------
## Update or Insert exixting data:   (Insert or update key of key Fav)
import json

file_name = "student.json"

# Step 1: Read the JSON file
with open(file_name, "r") as f:
    data = json.load(f)  # Load JSON content into a dictionary

# Step 2: Modify the data  !!! If you use same key to midify otherwise insert
data["Ebarat"]["Phone"] = "123456789"

# Step 3: Write the updated data back to the file
with open(file_name, "w") as f:
    json.dump(data, f, indent=4)

print("Phone number updated successfully!")


#-------------------------------------------------------------------------------

## delete Key from json file:   main key  (Del Fav)

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

##---------------------------------------------------------------------------------------------

## delete Key from json file: key of key    (Del Fav)

import json

data_file = "student.json"

# Load JSON from file
with open(data_file, "r") as f:
    data = json.load(f)

# data ["Ebarata"] .pop("City")
         # OR
if "City" in data["Ebarata"]:      # Fav
    del data["Ebarata"]["City"]

# Save the updated JSON back to the file
with open(data_file, "w") as f:
    json.dump(data, f, indent=4)

print(data)

##---------------------------------------------------------------------------------------------------
## Delete key of key of key:  (Del Fav)
import json

data_file = "student.json"

# Load JSON from file
with open(data_file, "r") as f:
    data = json.load(f)

if "ERR" in data["Anmals"]["Elephant"]:
    del data["Anmals"]["Elephant"]["ERR"]
# Save the updated JSON back to the file
with open(data_file, "w") as f:
    json.dump(data, f, indent=4)

print(data)



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

##----------------------------------------------------------------------------------------------------
## Make a Copy for other New Mai key Name:

import json

data_file = "student.json"

# Load JSON from file
with open(data_file, "r") as f:
    data = json.load(f)

if 'Ebarat' in data:
    data["Ebarata"]=data["Ebarat"]

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

#################################### SELF PRACTICE #####################################

# Create blank json file:
import json
data=""
with open ("Irfan.json","w")as f:
    x=json.dumps(f)

# Fill Data on Exixting file: !!!(Data will be replaced !)
import json
old_file="Irfan.json"
data={  "name":"Irfan", "gr_no":24928,"add":"BKC"
}
with open (old_file,"w") as f:
    x=json.dump(data,f)
#access data kay from file:
with open ("Irfan.json","r") as ff:
   j=json.load(ff)
   print(j.get("name"))

#--------------------------------------------------------------------------------

## Inser Data on Exixting file: !!!( If you use same key data will be replace )
import json
file="student.json"
with open (file,"r") as f:
    x=json.load(f)

x["Fruits"]={"aaple":763,"Grapes":665,"Pine":652}

with open (file,"w") as f:
    json.dump(x,f,indent=4)
print("Pine Price:")
print(x["Fruits"]["Pine"]) # Pine Price
# print(x)

#---------------------------------------------------------------------------------------

