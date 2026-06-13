def deposit(balance):
    amount=int(input("enter the amount"))
    balance+=amount
    return(balance)
def withdraw(balance):
        balance=balance-amount
        return(balance)
def bal(name,balance):
    print("name:",name)
    print("balance:",balance)
print("bank")
print("1.deposit")
print("2.withdraw")
print("3.balance")
print("4.exit")
name=input("enter the name:")
balance=int(input("enter the balance"))
ch=int(input("enter the choice:"))
while ch!=4:
    if ch==1:
       balance=deposit(balance)
    elif ch==2:
        amount=int(input("enter the amount"))
        if amount>balance:
            print("not possible")
        else:
            balance=withdraw(balance)
    elif ch==3:
        bal(name,balance)
    else:
        print("invalid choice")
    ch=int(input("enter the next choice"))
    