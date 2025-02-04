while True:
    name = input("Enter your name: ")
    if name == "":
        print("Name cannot be empty. Please enter a valid name.")
        continue
    
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Age must be a valid number. Please try again.")
        continue
    
    gender = input("Enter your gender: ")
    if gender == "":
        print("Gender cannot be empty. Please enter a valid gender.")
        continue
    
    print("Your name is",name)
    print("Your age is",age)
    print("You are ",gender)
    break