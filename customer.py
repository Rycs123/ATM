from atm_card import ATMCard


class Customer:
    def __init__(self, id, custPin=1234, custBalance=100000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def checkPin(self):
        return self.pin

    def checkBalance(self):
        return self.balance

    def checkId(self):
        return self.id

    def withdrawBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal
