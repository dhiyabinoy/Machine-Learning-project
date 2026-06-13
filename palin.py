def palindrome():
    str=input("enter the word")
    str1=str[::-1]
    if str1==str:
        print("palindrome")
    else:
        print("not palindrome")
palindrome()