#parent class/super class/ base class

class Animal:
    def sound(self):
        print("Animal is speaking")
# child class/ sub class/derived class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("cat is meowing")

a = Animal()
b = Dog()
b.sound()
c = Cat()
c.sound()


