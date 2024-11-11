import os
import time

inprogress = True
services = ['1','2']

class Bank:

    account_balance = 0
    deposition = ''
    withdrawal = ''

    def deposit(self):
        self.deposition = input("Please type the amount you would like to deposit:\n")
        try:
            self.deposition = float(self.deposition)
            self.deposition = round(self.deposition,2)
        except:
            print("Not a valid number.")
            return


        self.account_balance += self.deposition
        with open ('transaction_records.txt', 'a') as file:
            file.write(f'+ {self.deposition} ({time.ctime()})\nAccount Balance:\n{self.account_balance}\n')
        print(f"{self.deposition}$ deposited to user's account.")
        

    def withdraw(self):
        self.withdrawal = input("Please type the amount yu would like to withdraw:\n")
        try:
            self.withdrawal = float(self.withdrawal)
            self.withdrawal = round(self.withdrawal,2)
        except:
            print("Not a valid number.")
            return 
        

        if os.path.getsize('transaction_records.txt') == 0 or self.account_balance < self.withdrawal:
            print("There is not enough credit in your account.")
            return
        self.account_balance -= self.withdrawal
        with open ('transaction_records.txt', 'a') as file:
            file.write(f'- {self.withdrawal} ({time.ctime()})\nAccount Balance:\n{self.account_balance}\n')
        print(f"{self.withdrawal}$ withdrawn from user's account.")
        
        
        

print('Welcome to the bank !')

while(inprogress):
    transaction = input('''How may I assist you ?
                    1: I want to deposit.
                    2: I want to withdraw.\n''')

    if transaction not in services:
        print("Please, type a valid form of transaction.")
        continue

    if not os.path.isfile('transaction_records.txt'):
        with open('transaction_records.txt', 'w') as file:
            pass
    elif os.path.getsize('transaction_records.txt') == 0:
        pass
    else:
         with open('transaction_records.txt', 'r') as file:
            last_line = None
            for line in file:
                last_line = line
            try:    
                Bank.account_balance = float(last_line)
                Bank.account_balance = round(Bank.account_balance,2)
            except ValueError:
                print("Error reading account balance. Defaulting to 0.")


    transact = Bank()
    if transaction == '1':
        transact.deposit()
       
    else:
        transact.withdraw()
    
    print(f"Account's total balance: {transact.account_balance}$\n")
    morehelp = input("Can I help you with anything else ? (y/n)\n")
    if morehelp.lower() != 'y':
        print("Have a nice day !")
        inprogress = False

