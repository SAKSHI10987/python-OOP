class Atm:

    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()

    def menu(self):
        user_input=input("""
        1.set your pin.
        2.change you pin.
        3.withdraw the money.
        4.check balance.
        5.deposit money.
        """)

        if user_input=='1':
            #set pin
        elif user_input=='2':
            #change pin
        elif user_input=='3':
            #withdraw money
        elif user_input=='4':
            #check balance 
        elif user_input=='5':
            #deposit money
    
    def set_pin(self):
        self.pin=input("create a six digit pin")

        self.balance=input("enter you balance")
        print(f"your account is successfully created with pin number {self.pin} and balance {self.balance}")
    def change_pin(self):
        old_pin=input("enter your old pin!")
        new_pin=input("create you new six digit pin")

        self.pin=new_pin
        print(f"you pin number has been successfully changed from old pin {old_pin} to the current new pin {new_pin}")

    def withdraw(self):
        user=input("enter the amount you want to withdraw: ")
        bal=self.balance-user
        self.balance=bal

        print("amount is ")


obj=Atm()

