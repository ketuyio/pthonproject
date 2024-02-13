# A class is a blue print of an object
# An object is an instance of a class

class Person:
    # properties/attributes/characteristics/variables
    name = "Joe"
    age = 23
    #method/function/behavior
    def talk(self):
        print("Person is talking")


teacher = Person()
print(teacher.name)
print(teacher.age)

teacher.talk()
