try:
    print(x)
except:
       print("NameError occurred")
finally:
    print("success")

try:
    num1 = 20
    num2 = 0
    print(num1 / num2)
except:
    print("ZeroDivisionError occurred")
finally:
    print("success")

#user defined functions
try:
    def sum(first, second):
        return first + second
except:
    print("Exception occurred")
finally:
    print("success")
print(sum(10, 20))




