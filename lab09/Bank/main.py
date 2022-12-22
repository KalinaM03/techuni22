import random
class InvalidAccType(Exception):
    def __init__(self, message):
        self.message = message


class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message


class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message = message


class InvalidAccCurrency(Exception):
    def __init__(self, message):
        self.message = message


class UserNotFound(Exception):
    def __init__(self, message):
        self.message = message


class Bank:
    def __init__(self, users):
        self.users = list(users)


class User(Bank):
    def __init__(self, users, account, name, EGN):
        super().__init__(users)
        self.account = account
        self.name = name
        self.EGN = EGN

        if len(account) < 4:
            raise InvalidDataFormat('The name must be at least 4 characters long')

        if not EGN.isnumeric() or len(EGN)!=10:
            raise InvalidDataFormat('The EGN consists only of 10 DIGITS.')


class Account(User):
    def __init__(self, balance, currency, acc_type, IBAN):
        super().__init__(balance, currency, acc_type, IBAN)
        self.balance = balance
        self.currency = currency
        self.acc_type = acc_type
        self.IBAN = IBAN

        if type(balance)!=float:
            raise InvalidDataFormat('The balance must be a float')

        if currency!='BGN' and currency!='EUR' and currency!='USD' and currency!='JPY':
            raise InvalidAccCurrency("The only currencies supported are BGN, EUR, USD, and JPY")

        if acc_type!='current' and acc_type!='savings' and acc_type!='credit':
            raise InvalidAccType('The account can only be current, savings, or credit')


class Menu(Bank, User, Account):
    def print_menu(self):
        print("1. Create user")
        print("2. Create user account")
        print("3. List users")
        print("4. List accounts")
        print("5. Deposit")
        print("6. Withdrawal")
        print("7. Exit")

    def create_user(self, account):
        name=input('Enter first and last name: ')
        account=[]
        EGN=input('Enter your EGN: ')

        self.users.append(User(account, name, EGN))


    def create_user_acc(self):
        balance=float(input('Enter your balance: '))
        currency=input('Enter the currency of your account: ')
        acc_type=input('Enter account type: ')
        IBAN = f'BG9812{random.randrange(1000000000, 9999999999)}'

        self.account.append(Account(balance, currency, acc_type, IBAN))

    def run(self):
        self.print_menu()
        choice=int(input('Choose an option from the menu: '))
        while True:

            if choice==1:
                self.create_user()
            elif choice==2:
                self.create_user_acc()
            elif choice==3:
                print(self.users)
            elif choice==4:
                print(self.account)
            elif choice==5:
                pass
            elif choice==6:
                pass
            elif choice==7:
                break


if __name__ == '__main__':
    pass
