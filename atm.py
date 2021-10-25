class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber:cardnumber
        self.pin=pin
    def checkbalance(self):
        print("your Balance is 50,000,00")

    def withdrawl(self,amount):
        new_amount=50,000,00-amount
        print("you have withdrawn amount"+str(new_amount))

def main():
    cardnumber=input("insert your card number:- ")
    pinnumber=input("enter your pin number:- ")

    new_user =  Atm(cardnumber ,pinnumber)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()