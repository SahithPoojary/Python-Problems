def menu(Accounts,ch):
    while True:
        print("WELCOME TO ACCOUNT NUMBER {}".format(ch))
        print("1.CHECK BALANCE")
        print("2.DEPOSITE")
        print("3.WITHDRAW")
        print("4.TRANSFER")
        print("5.LOGOUT")
        d=int(input("Enter ur choice:"))
        if(d==1):
            print("Balance is:",Accounts[ch])
        elif(d==2):
            amt=int(input("Enter the amount to be deposited:"))
            deposite(Accounts,amt,ch)
        elif(d==3):
            am=int(input("Enter Withdraw Amount:"))
            withdraw(Accounts,am,ch)
        elif(d==4):
            to_acc=int(input("Enter the account number for which the amount should be sent:"))
            am=int(input("Enter the amount for the withdraw:"))
            transfer(Accounts,ch,to_acc,am)
        
        else:
            if d==5:
                break
            
def withdraw(Accounts,am,ch):
    if(am>Accounts[ch]):
        print("insufficient balance !!!")
    else:
        Accounts[ch]-=am

def transfer(Accounts,ch,to_acc,am):
    if(to_acc not in Accounts):
        print("No such account :(")
    else:
        if(am>Accounts[ch]):
            print("INSUFFICIENT BALANCE :(")
        else:
            Accounts[ch]-=am
            Accounts[to_acc]+=am
            print("Rs {} credited to {} from {}".format(am, to_acc,ch))

def deposite(Accounts,amt,ch):
    Accounts[ch]+=amt
    print("amount {} has been deposited to {}".format(amt,ch))

Accounts={101:1000,102:2000,103:3000}

while(True):
    print("--*BANK MANAGEMENT SYSTEM--*")
    ch=int(input("ENTER THE ACCOUNT NUMBER:"))
    if(ch in Accounts):
        menu(Accounts,ch)
    elif(ch==0):
        print("Exiting the system !!!! ")
        break
    else:
        print("Invalid!!")