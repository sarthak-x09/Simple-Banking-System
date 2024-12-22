import sys

BalanceA = 0
CaseV = 0

def checkCase():
    Case = 1
    return Case

def addDeposit(Amount):
    newBalance = BalanceA+Amount
    print(f"Your new balance is : {newBalance}")
    return newBalance 

def Withdraw(Amount):
    newBalance = BalanceA-Amount
    print(f"Your new balance is : {newBalance}")
    return newBalance

def Balance():
    if(CaseV == 1):
      BalanceA = newAmount
   
    elif(CaseV == 0):
        BalanceA = 0
    print("****************************")
    print(f"Your Balance is :{BalanceA}")    
    
while True:
    print("****************************")
    UserSel = int(input("Please select an option:\n1.Check Balance\n2.Withdraw\n3.Add Deposit\n4.Exit\nYour Option:"))

    if (UserSel == 1):
        Balance()

    elif(UserSel ==2):
        print("****************************")
        Amount = int(input("Please enter the amount:"))
        newAmount = Withdraw(Amount)
        BalanceA = newAmount
        CaseV = checkCase()

    elif(UserSel ==3):
        print("****************************")
        Amount = int(input("Please enter the amount:"))
        newAmount = addDeposit(Amount)
        BalanceA = newAmount
        CaseV = checkCase()
        
    elif(UserSel ==4):
        print("Exiting the Bank. Goodbye!")
        sys.exit
        break
        
