# class2.py

class Person:
    var1 = "My name is Timo Zandbergen and i am 16 years old"
    var2 = "I love playing soccer with my friends"
    var3 = 10.0
    var4 = True
    

    def var4truth(self):
        print(f"Is the question {Person.var4} or False.")   
  
    def printvar1(self):
        print(Person.var1)

    def printvar2(self):
        print(Person.var2)



class Student(Person):
    var5 = "You have a boost for 5 seconds"
    var6 = range(1, 6)

    def __init__(self):
        var1 = "Hello, how are you?"
        var4 = False
    
    def var4truth(self):
        print(f"The question is {Student.var4}.")
    
    def printvar1(self):
        super().printvar1()
        print("Hello how are you?")

    def printvar2(self):
        super().printvar2()
        print("I still like playing soccer with friends")                                                                                                                                                                                                                                                                                                                                                       


instanceA = Person()
instanceB = Student()

print(f"{instanceA.var1}.")
print(f"{instanceA.var2}.")
print(f"{instanceA.var3}.")
print(f"{instanceA.var4}.")
print(f"{instanceB.var5}.")
print(f"{instanceB.var6}.")

instanceA.var4truth()
instanceB.var4truth()
instanceB.printvar1()
instanceB.printvar2()
