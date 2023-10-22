class Bank:
    accounts = []
    account_number_count = 1000
    is_bankrupt = False
    total_balance = 0
    total_loan_balance = 0
    def __init__(self,name,email,address,password,type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.type = type
        self.AccNo = Bank.account_number_count
        Bank.account_number_count += 1
        self.balance = 0
        self.history = []
        self.loan_count = 0
        self.loan_limit = 5000

        if self.type in ['Current', 'Saving']:
            Bank.accounts.append(self)
        
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            Bank.total_balance += amount
            self.history.append(f"Deposit : {amount}")
            print(f"Successfully deposited Tk {amount}. Your current balance is {self.get_balance()}\n")
        else:
            print("Wrong amount, Enter amount correctly.\n")
    
    def withdraw(self,amount):
        if Bank.is_bankrupt:
            print("the bank is bankrupt.")
        elif amount > 0 and amount <= self.balance:
            self.balance -= amount
            Bank.total_balance -= amount
            self.history.append(f"Withdraw : {amount}")
            print(f"Successfully withdraw Tk {amount}. Your current balance is {self.get_balance()}\n")
        elif(amount > self.balance):
            print("Withdrawal amount Exceeds.\n")
        else:
            print("Wrong amount, Enter amount correctly.\n")
    
    def TakeLoan(self,amount):
        
        if amount > self.loan_limit:
            print(f"You cannot take loan more than Tk {self.loan_limit}\n")
        else:
            self.balance += amount
            self.loan_count += 1
            Bank.total_balance -= amount
            Bank.total_loan_balance += amount
            self.loan_limit -= amount
            print(f"Successfully taken loan of Tk {amount}")
            self.history.append(f"Taken Loan : {amount}")

    def ShowInfo(self):
        print(f"Showing info of {self.name}")
        print(f"    Account Name : {self.name}")
        print(f"    Account No : {self.AccNo}")
        print(f"    Account email : {self.email}")
        print(f"    Account address : {self.address}")
        print(f"    Account password : {self.password}")
        print(f"    Account balance : {self.balance}")
        print(f"    Account loan limit : {self.loan_count}")
        print(f"    Account taken loan : {self.loan_count}")
class CurAccount(Bank):
    def __init__(self, name, email, address, password) -> None:
        super().__init__(name, email, address,password,"Current")

class SavingAccount(Bank):
    def __init__(self, name, email, address, password, interest_rate) -> None:
        super().__init__(name, email, address, password, "Saving")
        self.interest_rate = interest_rate

CurUser = None
while(True):
    if CurUser == None:
        print("Login or Register first to use Banking system. \n")
        ch = input("Type 'R' for register or Type 'L' for Login : ").lower() 
        if ch == 'r':
            print("Which type of account you want to open. (Savings/Current) \n")
            acc_type = input("Type 'cr' for Current or Type 'sv' for Savings : ").lower()
            na = input("Enter your name : ")
            pasW = input("Enter an password : ")
            email = input("Enter your email : ")
            add = input("Enter your address : ")
            if acc_type == 'sv':
                iRate = int(input("Enter interest rate : "))
                NewAcc = SavingAccount(na,email,add,pasW,iRate)
                CurUser = NewAcc
                # Bank.accounts.append(NewAcc)
            else:
                NewAcc2 = CurAccount(na,email,add,pasW)
                CurUser = NewAcc2
                # Bank.accounts.append(NewAcc2)
        elif ch == 'l':
            accNo = int(input("Enter Account Number : "))
            passW = input("Enter Account Password : ")
            match = False
            for account in Bank.accounts:
                if account.AccNo == accNo and account.password == passW:
                    CurUser = account
                    match = True
                    break
            if match == False:
                print("No user found with this AccountNumber and Password. \n")
        else:
            ("Wrong option. Type an option correctly. \n")        
    
    
    elif(CurUser.name == "_admin_"):
        print(f"Wellcome admin. select an option what you want to do.\n")
        print(" 1. Create a new account.\n 2. Delete a user.\n 3. See all Users.\n 4. Check total available balance.\n 5. Check total loan balance.\n 6. Turn ON or OFF loan.\n 7. Logout")
        op = int(input("Enter your option : "))
        if op == 1:
            print("Which type of account you want to open. (Savings/Current) \n")
            acc_type = input("Type 'cr' for Current or Type 'sv' for Savings : ").lower()
            na = input("Enter your name : ")
            pasW = input("Enter an password : ")
            email = input("Enter your email : ")
            add = input("Enter your address : ")
            if acc_type == 'sv':
                iRate = int(input("Enter interest rate : "))
                NewAcc = SavingAccount(na,email,add,pasW,iRate)
                CurUser = NewAcc
                Bank.accounts.append(NewAcc)
            else:
                NewAcc2 = CurAccount(na,email,add,passW)
                CurUser = NewAcc2
                Bank.accounts.append(NewAcc2)
        elif op == 2:
            acno = int(input("Enter account number : "))
            ac_find = False
            for acc in Bank.accounts:
                if acc.AccNo == acno:
                    Bank.accounts.remove(acc)
                    print(f"Successfully deleted user account named {acc.name}.\n")
                    ac_find = True
                    break
            if ac_find == False:
                print("No user found with this account number.\n")
        elif op == 3:
            print("Showing All Users. \n")
            for acc in Bank.accounts:
                if acc.name == '_admin_':
                    continue
                print(f"Name : {acc.name}. email : {acc.email}. balance : {acc.balance} \n")
        
        elif op == 4:
            print(f"Total Bank balance is {Bank.total_balance}")
        elif op == 5:
            print(f"Total Bank loan balance is {Bank.total_loan_balance}")
        elif op == 6:
            if Bank.total_loan_balance > Bank.total_balance:
                Bank.is_bankrupt = True
        elif op == 7:
            CurUser = None
        else:
            print("Wrong option. Chose an option correctly. \n")

    else:
        print(f"\nWellcome {CurUser.name}. select an option what you want to do.\n")
        print(" 1. Show Balance.\n 2. Deposit Balance.\n 3. Withdraw Balance.\n 4. Transfer Balance.\n 5. Take loan.\n 6. Show history.\n 7. Show Account Info.\n 8. Logout.\n")
        opt = int(input("Enter your option : "))
        if opt == 1:
            print(f"Your current balance is {CurUser.get_balance()}")
        elif opt == 2:
            amount = int(input("Enter deposit amount : "))
            CurUser.deposit(amount)
        elif opt == 3:
            amount = int(input("Enter withdraw amount : "))
            CurUser.withdraw(amount)
        elif opt == 4:
            acno = int(input("Enter Transfer account number : "))
            found = False
            for acc in Bank.accounts:
                if acc.AccNo == acno:
                    found = True
                    tk = int(input("Enter transfer amount : "))
                    if tk > 0 and tk <= CurUser.get_balance():
                        acc.balance += tk
                        CurUser.balance -= tk
                    else:
                        "Wrong Amount"
                    break
            if found == False:
                print("Accunt does not exist. \n")
        elif opt == 5:
            if CurUser.loan_count <= 2:
                amnt = int(input("Enter loan amount : "))
                CurUser.TakeLoan(amnt)
            else:
                print("You can't take loan upto 2 times.\n ")
        elif opt == 6:
            for his in CurUser.history:
                print(f" {his}")
        elif opt == 7:
            CurUser.ShowInfo()
        elif opt == 8:
            CurUser = None
        else:
            print("Wrong option. Chose an option correctly. \n")