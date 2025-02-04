class Student:
    def setdata(self):
        self.name=input("Enter name: ")
        self.roll=int(input("Enter Roll: "))
        self.per=float(input("Enter Percenntage: "))
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.roll)
        print("Percentage",self.per)
a=Student()
a.setdata()
a.display()