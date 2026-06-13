limit=int(input("enter the limit"))
a=0
b=1
if limit==1:
    print(a)
elif limit==2:
    print(a,b)
    print(c)
else:
    print(a)
    print(b)
    for i in range(0,limit-2):
        result=a+b
        a=b
        b=result
        print(result,"\t")       
        