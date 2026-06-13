n=int(input("enter the no:"))
fact=1
if n==0:
    print("factorial:",fact)
else:
    for i in range(1,n+1):
         fact *=i
    print("fact",fact)