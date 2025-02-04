while True:
    name=input("Enter your name: ")
    if name.strip():
        print("Hello",name)
        break
    else:
        # pass (if you want Empty)
        print("Dont leave Empty!")