def addition(a,b):
   sum=a+b
   print(sum)
def subtraction(a,b):
   diff=a-b
   print(diff)
def multiplication(a,b):
    mult=a*b
    print(mult)
def division(a,b):
     if b==0:
        print("cannot divide")
     else:
        div=a/b
        print(div)
print("calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exit")
ch=int(input("enter the choice"))
while ch!=5:
    a=int(input("enter the no:"))
    b=int(input("enter the no:"))
    if ch==1:
        addition(a,b)
    elif ch==2:
        subtraction(a,b)
    elif ch==3:
        multiplication(a,b)
    elif ch==4:
        division(a,b)
    else:
        print("invalid choice")
    ch=int(input("enter the next choice"))
if ch==5:
    print("exit..")