class Person:
  def __init__(myself, name, age, hobby, length):
    myself.name = name
    myself.age = age
    myself.hobby = hobby
    myself.length = length

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print("I am " + abc.age + " years old")
    print("I like playing " + abc.hobby + " with my soccer team")
    print("I am " + abc.length + " tall ")
p1 = Person("Timo", "16", "soccer", "1.93" )
p1.myfunc()







        




