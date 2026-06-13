str=input("enter the sting:")
str1=("a","e","i","o","u","A","E","I","O","U")
count=0
for i in str:
    if i in str1:
        count+=1
print("vowels:",count)