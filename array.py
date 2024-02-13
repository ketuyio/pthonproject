courses = ["MIT","cybersecurity","Data Science"]
print(courses)

#accessing an element in an array
print(courses[1])

#looping through an array
for course in courses:
    print(course)

#adding a new element in an array
courses.append("android programming")
print(courses)

#deleting an element from an array
courses.remove("Data Science")
print(courses)