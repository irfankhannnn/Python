# Summery of List Tuple Dictnary & Sets:
# List is use []
# Tuple use () & Immutable also irrepeatable.
# Set use set keyword like # set1=set([]) & {}
# Dict use {}  key is Immutable like 1: Jan 1 is key. U can appand value but not insert. 










# List / Array
# Imp keys Append, Insert, Remove -user Num or Str & pop -use positin:
stock_price=[554,676,264,254]
print("Stocks: ",stock_price[1])
 
#---------------------------------------------------------------------------------------------------------------------
# Yearly Expance

# Know Monthly Expence Jan & Fab:
exp=[210,549,944,954,722,345]
print("Jan and fab Expences: ",exp[0]+exp[1])


# Findout 3000 spend in any month:
print("Did i spend 3000 in any month?",3000 in exp)
# Output: False


# June month is just finish and i want add 432 for Jully
exp.append(432)

# March Expense = April
exp[3]=exp[2]

# Lets Minus 44 rupees in March:
exp[2]=exp[2]-44  # 944-44
print(exp)
# Output: 900

#---------------------------------------------------------------------------------------------------------------------

# Create List of Fruits:
fruits=["apple",'banana','berrys','greaps']

## Find length:
# print(len(fruits))  

## Append fruits:
fruits.append("Mango")

#-------------------------------------------
rank=[56,45,32,33,24,78,35]
rank.append(99)
rank[1]=892
rank.remove(24) #removr 24 from list.
rank.pop(1) # (1) is position
rank.insert(0,3) #Inser start of list. 0 is psition
print(rank)
#-------------------------------------------

## Remove fruit
# fruits.remove("apple")

# position list of 2:
fruits.insert(2,"pine")

#  Lets remove banana & pine and replace with kiwi:
fruits[1:3]=["kiwi"]

##P print first 2 fruits
# print(fruits[:2])

## print without symbols:
# print(*fruits[:2]) 

## Sort in alphabatical order:
fruits.sort()

print(*fruits)
#---------------------------------------------------------------------------------------------------------------------
# Create Programm max numbers Odd numbers using List:

max = int(input("Ente max number: "))

odd_numbers=[]
for i in range(1,max):
    if i%2==1:
        odd_numbers.append(i)
print("Odd Numbers: ", odd_numbers)

#---------------------------------------------------------------------------------------------------------------------
import random
my_list = [1, 2, 3, 4, 5]

# Print list elements
print("List elements:", *my_list)

# Get a random element from the list
random_element = random.choice(my_list)
print("Random choice:", random_element)

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
# Dictnory
stock_price={
    'Jan':43,
    'fab':75,
    'mar':76,
}

## Adding or updating Valur:
stock_price['apr']=42

## Removing Elements using del:
del stock_price["Jan"]

## Removing Element using pop:
mar=stock_price.pop("mar")

print("Stocks: ",stock_price['Jan'])


#--------------------------------------------------------------------------------------------------------------------


## Adding multiple list in Dictnary:
student=[
    {"Name": "Irfan","Age":54,"Gender":"Male"},
    {"Name":"Amir","Age":24,"Gender":"Male"},
        ]

## Adding new Student:

print(student)
student.append({"Name":"Avesh","age":43,"Gender":"Male"})


#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# Tuple is Imuteable jaise not changeable.


#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# Set is irrepeatable value.

set1=set([5,3,8,7,8,6,4,9,5,4])
set2={4,3,5,7,5,3,2,4,5,4,6,9}

print(set1)
print(set2)