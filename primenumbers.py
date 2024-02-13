num = 12
if num > 1:
    for x in range(2, num):
        if num % x == 0:
            print("Not Prime Number")
        else:
            print("Prime Number")
            break
    else:
       print("Not Prime Number")
