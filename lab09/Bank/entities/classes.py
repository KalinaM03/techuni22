class Bank:
    def __init__(self, users):
        self.users = users


class User:
    def __init__(self, account, name, EGN):
        self.account=account
        self.name=name
        self.EGN=EGN

        if len(account)<4:
            raise In


class Account:
    def __init__(self, balance, currency, acc_type, IBAN):
        self.balance=balance
        self.currency=currency
        self.acc_type=acc_type
        self.IBAN=IBAN