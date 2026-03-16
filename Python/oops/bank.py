class Bank :

    acc_num : int
    name : str
    acc_type : str
    balance : int

    def create_acc(self,acc_num,name,acc_type,balance):

        self.acc_num = acc_num
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self,amount) :

        self.balance += amount

        print(f"your account{self.acc_num} credited with amount {amount}.your avl bal is {self.balance}")

    def withdraw(self,amount) :

        if amount<self.balance :

            self.balance -= amount

            print(f"your account{self.acc_num} debited with amount {amount}.your avl bal is {self.balance}")
        else :

            print("insufficient balance")

    def show_balance(self) :


        print(f"hai{self.name} your acc bal is {self.balance}")

bank_acc_instance = Bank()

bank_acc_instance.create_acc(12344556,"Abhi","current ac",1000)

bank_acc_instance.deposit(4000)

bank_acc_instance.withdraw(2000)

bank_acc_instance.show_balance()


