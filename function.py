# Inbuilt functions
number = max(34,28,47,131,24,67)
print(number)

y = min(34,28,47,131,24)
print(y)

z = pow(2,3)
print(z)

# user defined functions
def name():
    print("Elias")
name() # calling a function

def details():
    name = "Aziz"
    age = 17
    course = "MIt"
    print(name,age,course)
details()

# parameters/variables and arguments
def patient(name,gender,age,mariage_status):
    print(name,gender,age,mariage_status)
patient("Job","Male","25","single")
patient("Mary","Female","23","married")
patient("James","Male","34","married")
patient("Jolene","Female","28","single")

def multiply(x,y):
    print(x*y)
multiply(10,20)
multiply(14,50)
multiply(60,29)
multiply(4,34)
multiply(15,26)

# creat a user defined function called employees.
# Display details of 5 employees using these parameters:fullname,age,position,salary
def emloyees(fullname,age,position,salary):
    print(fullname,age,position,salary)
emloyees("Jonas_maliki","34","secretary","70,000")
emloyees("Lucy_malo","25","Artilary_manager","50,000")
emloyees("Troon_Groski","44","manager","120,000")
emloyees("Moses_Omolo","29","treasurer","90,000")
emloyees("margarate_Tunde","34","chief_executive","150,000")

