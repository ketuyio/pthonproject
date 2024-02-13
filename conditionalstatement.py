temperature = 34

if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# A program that determines the largest number among three numbers
num1 = 78
num2 = 98
num3 = 23
if num1 > num2 and num1 > num3:
    print(num1, "Is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "Is the largest number")
else:
    print(num3, "Is the largest number")

# a program that checks whether a number is even or odd
num = 47
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# a program that shows whether a number is prime or not
num = 20
# If given number is greater than 1
if num > 1:
    for i in range(2, int(num/2)+1):
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")

