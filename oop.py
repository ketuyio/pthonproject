class person:
    def __init__(self,firstname,lastname,age,gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
    def details(self):
        print(self.firstname,"Is studying")

teacher = person("John","Mbugua",24,"Male")
accountant = person("Mary","Naliaka",27,"Female")
doctor = person("Joe","Mboga",44,"Male")
driver = person("Julian","travis",35,"Male")
nurse = person("Jenifer","Nandwa",26,"female")
manager = person("Christopher","Maluki",53,"Male")
print(teacher.firstname,teacher.lastname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.lastname,accountant.age,accountant.gender)
teacher.details()
