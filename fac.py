def facto(num):
    fact=1
    if num==0:
        return 1
    else:
        fact=num*(facto(num-1))
        return(fact)
num=int(input("enter the number:"))
factorial=facto(num)
print(factorial)