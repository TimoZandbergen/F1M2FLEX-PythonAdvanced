# inheritance.py

class Person:
    var1 = "My name is Timo Zandbergen and i am 16 years old"
    var2 = 0
    var3 = 10.0
    var4 = True

    def var4truth(self):
        print(f"var4 in Class Person is {Person.var4}.")   
  
    def printvar1(self):
        print(Person.var1)



class Student(Person):
    var5 = [1, 2, 3]
    var6 = range(1, 6)

    def __init__(self):
        var1 = "There is now text here"
        var4 = False
    
    def var4truth(self):
        print(f"var4 is now {Student.var4} in Class Student.")
    
    def printvar1(self):
        super().printvar1()
        print("This function was put in class B, and therefore has been updated to display this text by using the super() function.")

instanceA = Person()
instanceB = Student()

print(f"Variable 1 of Class Person is {instanceA.var1}.")
print(f"Variable 2 of Class Person is {instanceA.var2}.")
print(f"Variable 3 of Class Person is {instanceA.var3}.")
print(f"Variable 4 of Class Person is {instanceA.var4}.")
print(f"Variable 5 of Class Student is {instanceB.var5}.")
print(f"Variable 6 of Class Student is {instanceB.var6}.")

instanceA.var4truth()
instanceB.var4truth()
instanceB.printvar1()