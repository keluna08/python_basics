class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES has been successfully send to {recipient}")
        else:
             print("Insufficient balance")


# child class1
class PersonalMpesa(Mpesa):
    def __init__(self,account_balance, phone_number,id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buyairtime(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES has been credited. The balance is {self.account_balance}")
        else:
            print("Insufficient balance")

# child class2
class BusinessMpesa(Mpesa):
    def __int__(self,account_balance, phone_number,business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name

    def receivemoney(self,amount):
        self.account_balance += amount
        print(f"{amount} KES has been received your balance is {self.account_balance}")



personal=Mpesa(2000,73456789)
personal.send_money(1500,734522347)

# instance for buyairtime
personalob=PersonalMpesa(2000,72343455,43526)
personalob.buyairtime(100)

# instance for business
received=BusinessMpesa(3000,7345789)
received.receivemoney(2000)





