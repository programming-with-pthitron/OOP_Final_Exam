class Person:
   
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        

        

    def __repr__(self) -> str:
        return f"email: {self.username}, ID:  {self.user_id}"
class Balance:
    def __init__(self, username, balance) -> None:
        self.username = username
        self.balance = balance

class History:
    def __init__(self, username) -> None:
        self.username = username
        self.deposit = 0
        self.withdraw = 0
        self.transfar = 0
        self.loan = 0

class Bank:
    user_list = []
    user_balance = []
    user_transaction_history = []

    def __init__(self):
        
        self.balance = 0
        self.total_loan = 0
        self.loan_feature = True
    
    def get_users(self):
        return self.user_list

    def create_account(self):
        print("Create Your New Bank Account...")
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        self.transfar_history(username)
        self.user = Person(username, password)
        self.user_list.append(vars(self.user))

    def transfar_history(self, username):
        print(username)
        self.history = History(username)
        self.user_transaction_history.append(vars(self.history))
    
    def deposit_amount(self, username, amount):
        self.amount = amount
        self.username = username
        flag = True
        for w in self.user_balance:
            if username == w['username']:
                w['balance'] += amount
                flag = False
        if flag:
            for w in self.user_list:
                if username == w['username']:
                    self.add_amount = Balance(username, amount)
                    self.user_balance.append(vars(self.add_amount))

                
        for i in self.user_transaction_history:
            if i['username'] == username:
                i['deposit'] += amount
                

        self.balance = self.balance + amount
        print("successfully deposit amount ", amount)
    
    def withdraw_amount(self,username, amount):
        self.amount = amount
        for w in self.user_balance:
            if username == w['username']:
                d = True
                if w['balance'] < amount:
                    print("Insufficient balance")
                else:
                    w['balance'] -= amount
                    self.balance -= amount
                    print("withdraw amount ", amount)
                    for i in self.user_transaction_history:
                        if i['username'] == username:
                            i['withdraw'] += amount
    
    def check_balance(self, username):
        for w in self.user_balance:
            if username == w['username']:
                print("user Balance is", w['balance'])
            
    
    def check_total_balance(self):
        print("Total bank balance", self.balance)

    def transfer_balance(self, from_username, amount, to_username):
        self.from_username = from_username
        self.amount = amount
        self.to_username = to_username
        tm = True
        for w in self.user_balance:
            if w['username'] == from_username:
                tm = False
                flag = True
                for y in self.user_balance:
                    if y['username'] == to_username:
                        y['balance'] += amount
                        w['balance'] -= amount
                        print("balance transfarr successfull")
                        for i in self.user_transaction_history:
                            if i['username'] == from_username:
                                i['transfar'] += amount
                        flag = False
                if flag:
                    print(f"{to_username} account not fount")
        if tm:
            print(f"{from_username} account not found")

    def transaction_history(self, username):
        for w in self.user_transaction_history:
            if w['username'] == username:
                print(f"diposit : {w['deposit']} withdraw : {w['withdraw']} transfar_balance : {w['transfar']} bank_loan : {w['loan']} ")

        
    def bank_loan(self, username, amount):
        if self.loan_feature:
            for w in self.user_balance:
                if w['username'] == username:
                    if w['balance']*2 >= amount:
                        print(f"loan successfull")
                        self.balance -= amount
                        self.total_loan += amount
                        for i in self.user_transaction_history:
                            if i['username'] == username:
                                i['loan'] += amount
        
        else:
            print(" SORRY Loan Feature is off")
        
    
    def total_loan_amount(self):
        print("total_loan_amount: ", self.total_loan)
    
    def bank_loan_feature(self, feature):
        if feature == 'on':
            self.loan_feature = True
        else:
            self.loan_feature = False


while True:
    bank = Bank()
    print(f"1. User\n2. Admin\n")
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        while True:
            print("1. ----Exit----\n")
            ex = int(input("tap to 1 and exit: "))
            if ex == 1:
                break
            bank.create_account()
            print("Login to your account...")
            name = input("Enter your username: ")
            password = input("Enter your password: ")

            for w in bank.get_users():
                if w['username'] == name and w['password'] == password:
                    print("------Welcome to our bank------\n")
                    print(f"1. Deposit Amount----\n2. Withdraw Amount----\n3. Check available balance----\n4. Transfer Amount----\n5. Check transaction history----\n6. Take Loan-----\n7. Exit \n")
                    b = int(input("Enter your choice: "))
                    if b == 1:
                        amount1 = int(input("Enter your amount: "))
                        bank.deposit_amount(name, amount1)
                    elif b == 2:
                        amount2 = int(input("Enter your amount: "))
                        bank.withdraw_amount(name, amount2)
                    elif b == 3:
                        bank.check_balance(name)
                    elif b == 4:
                        amount4 = int(input("Enter transfer amount: "))
                        name2 = input("Enter to_username: ")
                        bank.transfar_balance(name, amount4, name2)
                    elif b == 5:
                        bank.transaction_history(name)
                    elif b == 6:
                        amount6 = int(input("Enter Loan amount: "))
                        bank.bank_loan(name, amount6)
                    elif b == 7:
                        break

                    

    else:
        while True:
            print("1. ----Exit----\n")
            ex = int(input("Enter exit number: "))
            if ex == 1:
                break
            name = input("Enter your username: ")
            password = input("Enter your password: ")

            isAdmin = False
            if name == 'admin' and password == '1234':
                print("----Welcome to Admin pannel----\n")
                print(f"1. Check the total available balance..\n2. Check the total loan amount..\n3. Loan feature..\n4. Exit")
                admin_input = int(input("Enter your choice: "))
                if admin_input == 1:
                    bank.check_total_balance()
                elif admin_input == 2:
                    bank.total_loan_amount()
                elif admin_input == 3:
                    f = input("Enter loan feature: ")
                    bank.total_loan(f)   
                elif admin_input == 4:
                    break         

            
        
""" print("Login your account")






bank = Bank()
bank.create_account()
bank.deposit_amount('jony',400)
bank.withdraw_amount('jony',200)
bank.check_balance('jony')
bank.create_account()
bank.deposit_amount('rony',700)
bank.withdraw_amount('rony',600)
bank.check_balance('rony')

bank.deposit_amount('jony',400)
#bank.withdraw_amount('jony',200)
bank.check_balance('jony')
bank.check_total_balance()
bank.transfer_balance('jony',300, 'rony')
bank.check_balance('jony')
bank.check_balance('rony')
print(bank.transaction_history('rony'))
bank.bank_loan('jony',22)
print(bank.transaction_history('jony'))
bank.bank_loan_feature('off')
bank.bank_loan('rony',222)
bank.total_loan_amount()

print(bank.get_users())
"""