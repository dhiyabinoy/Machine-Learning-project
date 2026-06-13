file=open("sample.txt",'w')
file.write("welcome")
a=file.tell()
print(a)
file.seek(2)
file.close