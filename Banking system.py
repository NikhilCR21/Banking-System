import random
import sys
from account_details import Account

class Bankaccount:
    def __init__(self):
        print("Welcome to the banking system")
        print("1. Already a user\n2. New user")
        a = int(input("Enter your option: "))
        if a == 1:
            b = input("Enter your account number : ")
            c = int(input("Enter the password: "))
            self.user = b
            self.pw = c
            self.login()
        elif a == 2:
            self.new_user()
        else:
            print("Enter a valid number\n")
            self.__init__()

    def login(self):
        if self.user in Account and self.pw == Account[self.user]['pw']:
            print("1. Balance enquiry\n2. Withdrawal\n3. Deposit\n4. Change pin\n5. Cancel transaction")
            num1 = int(input("Enter your number: "))
            if num1 == 1:
                self.balance()
            elif num1 == 2:
                self.withdrawal()
            elif num1 == 3:
                self.deposit()
            elif num1 == 4:
                self.change_pin()
            elif num1 == 5:
                self.cancel()
                sys.exit()
            else:
                print("Enter a valid number ")

    def balance(self):
        print("Current balance is: ", Account[self.user]['balance'])
        self.login()

    def withdrawal(self):
        amount = int(input("Enter the amount to withdraw: "))
        if 0 < amount < Account[self.user]['balance']:
            Account[self.user]['balance'] -= amount
            print("Withdrew:", amount, "Current balance is:", Account[self.user]['balance'])
            self.update_account_details()
            self.login()
        elif amount >= Account[self.user]['balance']:
            print("Transaction is not possible, enter any other amount")


    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            Account[self.user]['balance'] += amount
            print("Your balance amount is:", Account[self.user]['balance'])
            self.update_account_details()
            self.login()

    def change_pin(self):
        pa = int(input("Enter the new pin: "))
        if 0 <= pa <= 9999:
            Account[self.user]["pw"] = pa
            print("Pin changed successfully")
        self.update_account_details()
        self.login()

    def cancel(self):
        print("Cancelling the transaction ")
        exit()

    def new_user(self):
        name = input("Enter your name: ")
        acc_no = random.randint(10001,99999)
        print(f"Your Account number is : {acc_no}")
        account_no = str(acc_no)
        password = int(input("Enter the password: "))
        password = int(input("Renter the password: "))
        balance = 0
        print("You have successfully created your account ")
        print(f"Your account number is: {account_no}")
        if account_no not in Account:
            Account[account_no] = {'name': name.lower(), 'acno': account_no, 'pw': password, 'balance': balance}
        self.update_account_details()

    def update_account_details(self):
        with open("account_details.py", "w") as file:
            file.write(f"Account = {Account}\n")


B = Bankaccount()
B.__init__()