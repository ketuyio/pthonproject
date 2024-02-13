#Data type

number = 67 # int
num = 78.98 # float
greeting = "Hello there" #str
IsPythonInteresting = True #bool

# A variable storing multiple values
languages = ["Python","PHP","JavaScript"] #list
fruits = ["banana","apple","orange"] #tuple
countries = {"kenya","Bangladesh","China","France","Mexico"}
#dictionary
details = {
    "firstname" : "Brian",
    "age": 17,
    "course":"MIT",
    "nationality":"Kenya",

}
print(number)
print(IsPythonInteresting)
print(countries)
print(details)
print(details["course"])

#determining the data type
print(type(details))
print(type(countries))
print(type(languages))

#  typecasting-converting one data type to another
print(float(number))
print(int(num))





