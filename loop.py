#while loop
# incrementing
number = 20
while number <= 25:
    print(number)
    number += 1

#decrementing
num = 105
while num >= 100:
    print(num)
    num -=1

#break statement
x = 30
while x <= 40:
    print(x)
    if x == 36:
        break
    x +=1

# continue
y = 29
while y <= 35:
    y += 1
    if y == 32:
        continue
    print(y)

# for loop
languages = ['Python', 'Java', 'C++']
for lang in languages:
    print(lang)

# RANGE
for mynumber in range(6):
    print(mynumber)

for mynum in range(20,28):
    print(mynum)

for z in range(20,30,3):
    print(z)

