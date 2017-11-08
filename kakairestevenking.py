import time
class Bank(object):
    def __init__(self, BankId, Name, Location):
        self.BankId = BankId
        self.Name = Name
        self.Location = Location
        pass



class Teller(Bank):
    teller_balance = 0  # The nitial amount collected by teller 
    account_number1 = 2910000  # the first account number given out
    account_dictionary = {}
    Records=[]      #List stores transaction time and date by teller

    def __init__(self, teller_id, teller_name, BankId, Name, Location):
        super().__init__(BankId, Name, Location)
        #assert teller_id == int and teller_name == str
        self.Teller_id = teller_id
        self.Teller_name = teller_name

    def CollectMoney(self,amount):  # exception required
        self.amount=amount 
        Teller.teller_balance += self.amount
        print("Teller balance =",Teller.teller_balance)
        Teller.Records.append("Collected")
        Teller.Records.append(self.amount)
        Teller.Records.append(time.asctime( time.localtime(time.time())))

    def OpenAccount(self,name, account_type ):
        Teller.account_number1 += 1
        account_details = {Teller.account_number1:name}
        Teller.account_dictionary.update(account_details)
        print("Thank you for opening an account with us \n\nAccount details...\nAccount Type: ", account_type,
              "\nAccount Name: ", name, "Account Number ", Teller.account_number1)
        Teller.Records.append("Opened the account")
        Teller.Records.append(Teller.account_number1)
        Teller.Records.append(time.asctime( time.localtime(time.time())))

    def CloseAccount(self,account_number):
        try:
            del Teller.account_dictionary[account_number]
            print("Account successfully deleted")
            Teller.Records.append(" Closed account")
            Teller.Records.append(account_number)
            Teller.Records.append(time.asctime( time.localtime(time.time())))
        except:
            print("Account doest exist")

    def RequestLoan(self):  # exception required
        loan_amount = int(input("Loan amount"))
        asset_value = int(input("Asset Value"))
        if asset_value >= 2*loan_amount:
            print("the customer may apply for the loan")
        else:
            print("the customer does not qualify for the given loan ")

    def ProvideInfo(self):  # exception
        response = int(input("Enter:\n1. Account opening info\n2. loan info\n3. Promotions"))
        if response is 1:
            print("Account opening requirements\n3 passport photos\nNational ID\n 50,000/= min deposit")
        if response is 2:
            print("The loan applicant must have an asset value of at least twice the the requested loan amount")
        if response is 3:
            print("We currently have no running promotions ")

    def IssueCard(self):  # except
        response = int(input("enter time elapsed(in weeks) since card request"))
        if response >= 2:
            print("kindly pick your card from the accounts section ")
        else:
            x = 2 - response
            print("The card will be available in", x, "weeks")


class Customer(Bank):
    Records = [] # List stores transaction time and date by customer
    def __init__(self,Id,CustomerName,Address,PhoneNo,AccountNo,BankId, Name, Location):
        super().__init__(BankId, Name, Location)
        self.CustomerName=CustomerName
        self.Address=Address
        self.PhoneNo=int(PhoneNo)
        self.AccountNo=int(AccountNo)
        self.balance=0

    def GeneralInquiry(self):
        print('Name:', self.Name,'\n Address: ',self.Address,'\n PhoneNo: ',self.PhoneNo,'\n AccountNo: ',self.AccountNo,'\n Accountbal: ',self.balance)

    def DepositMoney(self,amount):
        self.amount=amount
        self.balance+=amount
        Customer.Records.append("Deposited")
        Customer.Records.append(self.amount)
        Customer.Records.append(time.asctime( time.localtime(time.time())))
        print("your account balance is", self.balance)
      
    
    def WithdrawMoney(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("you have insufficient funds")
        else:
            self.balance-=self.amount
            Customer.Records.append("Withdrew")
            Customer.Records.append(self.amount)
            Customer.Records.append(time.asctime( time.localtime(time.time())))
        print("your account balance is", self.balance)
        
    def OpenAccount(self,Id,CustomerId):
        self.Account=Account(Id,CustomerId)
        
    def ApplyForLoan(self,Id,Type,AccountId,CustomerId,amount):
        #Customer fills in the laon application form
        self.Loan=Loan(Id,Type,AccountId,CustomerId) #new object assigned to Loan class
        self.Loan.ApplyForLoan(amount)
        
        
    def RequestCard():
        print( "Your card is being processed")

class Account(Customer):
    Records=[]      #List stores accounts transaction times and dates
    def __init__(self,Id,CustomerId):
        super(Account).__init__(Customer)
        self.Id=int(Id)
        self.CustomerId=int(CustomerId)
        self.balance=0
        
    def DepositMoney(self,Id,CustomerId,amount):
        #customer specifies savings or checking account Id, Customer Id and deposit amount
        response=int(input('Enter \n1 for Savings account \n2 for Checking account: \n'))
        
        if response==1:
            self.Savings=Savings(Id,CustomerId)
            #object assingned for Savings account
            self.Savings.DepositMoney(amount)
            Account.Records.append("Savings account deposit of")
            Account.Records.append(amount)
            Account.Records.append(time.asctime( time.localtime(time.time())))

        elif response==2:
            self.Checking=Checking(Id,CustomerId)
            #object assingned for Checking account
            self.Checking.DepositMoney(amount)
            Account.Records.append("checking account of")
            Account.Records.append(amount)
            Account.Records.append(time.asctime( time.localtime(time.time())))
        else:
            print("You entered an invalid input")
        
    
    def WithdrawMoney(self,Id,CustomerId,amount):
        #customer specifies savings or checking account Id,Customer Id and withdraw amount
        response=int(input('Enter \n1 for Savings account \n2 for Checking account:\n '))
        
        if response==1:
            self.Savings=Savings(Id,CustomerId)
            #object assingned for Savings account
            self.Savings.WithdrawMoney(amount)
            Account.Records.append("Savings account withdraw of")
            Account.Records.append(amount)
            Account.Records.append(time.asctime( time.localtime(time.time())))

        elif response==2:
            self.Checking=Checking(Id,CustomerId)
            #object assingned for Checking account
            self.Checking.WithdrawMoney(amount)
            Account.Records.append("Checkings account withdraw of")
            Account.Records.append(amount)
            Account.Records.append(time.asctime( time.localtime(time.time())))
        else:
            print("You entered an invalid input")
        

class  Loan(Customer):
    Records=[]      #List stores loan transaction times and dates
    loan=0
    balance=0
    def __init__(self,Id,Type,AccountId,CustomerId):
        super(Loan).__init__(Customer)
        self.Id=Id
        self.Type=Type
        self.AccountId=AccountId
        self.CustomerId=CustomerId
        
    def ApplyForLoan(self,amount):
        self.amount=amount
        Loan.loan+=self.amount
        
        print("You have borrowed: ",self.amount,' Uganda shilings')

    def DepositMoney(self,amount):
        #The amount deposited in the laon account is to pay loan 
        self.amount=amount
        if self.amount==Loan.loan:
            Loan.loan=0
            print ("Loan cleared")
            Loan.Records.append("Loan amount paid:")
            Loan.Records.append(self.amount)
            Loan.Records.append(time.asctime( time.localtime(time.time())))
        elif self.amount>Loan.loan:
            Loan.balance=self.amount-Loan.loan
            Loan.loan=0
            print( "Loan cleared")
            print ("Excess amount: ",Loan.balance)
            Loan.Records.append("Loan amount paid:")
            Loan.Records.append(self.amount)
            Loan.Records.append(time.asctime( time.localtime(time.time())))
        else:
            Loan.balance=Loan.loan-self.amount
            Loan.loan=abs(Loan.balance)
            print ("Your loan balance is: ",Loan.balance)
            Loan.Records.append("Loan amount paid:")
            Loan.Records.append(self.amount)
            Loan.Records.append(time.asctime( time.localtime(time.time())))
        
class Checking(Account):
    balance=0
    def __init__(self,Id,CustomerId):
        super(Savings).__init__(Account)
        self.Id=Id
        self.CustomerId=CustomerId
        
        
    def DepositMoney(self,amount):
        self.amount=amount
        Checking.balance+=self.amount
        print( "Your Checking Account balance is: ",Checking.balance)
    
    def WithdrawMoney(self,amount):
        self.amount=amount
        if self.amount>Savings.balance:
            print("Amount greaterthan available balance")
        else:
            Checking.balance-=self.amount
        print ("Your Checking Account balance is: ",Checking.balance)
        

class Savings(Account):
    balance=0
    def __init__(self,Id,CustomerId):
        super(Savings).__init__(Account)
        self.Id=Id
        self.CustomerId=CustomerId
        
        
    def DepositMoney(self,amount):
        self.amount=amount
        Savings.balance+=self.amount
        print( "Your Savings Account balance is: ",Savings.balance)
    
    def WithdrawMoney(self,amount):
        self.amount=amount
        if self.amount>Savings.balance:
            print("Amount greaterthan available balance")
        else:
            Savings.balance-=self.amount
        print ("Your Savings Account balance is: ",Savings.balance)

        

        

bank1=Bank(1122,'Stanbic','Makerere')
bank2=Bank(1023,'centenary','Nakawa')

teller1=Teller(204,'Kakaire Steven',4040,'Stanbic','Makerere')
teller2=Teller(205,'Akena Gibbs',4040,'Stanbic','Makerere')
teller3=Teller(206,'Hareza Sarah',4040,'Stanbic','Makerere')
teller4=Teller(207,'Tamale Joel',8080,'Centenary','Kampala')
teller5=Teller(208,'Terence Micheal',8080,'Centenary','Kampala')
teller6=Teller(209,'Aropu Isaac',8080,'Centenary','Kampala')

customer1=Customer(1001,'Anying Benjamin','Kampala',773434343,20020141565,4040,'Stanbic','Makerere')
customer2=Customer(1202,'Akenu Esther','Kampala',772200552,200205566,4040,'Stanbic','Makerere')
customer3=Customer(1211,'Okello Titus','Kampala',773434300,200203644,4040,'Stanbic','Makerere')
customer4=Customer(1231,'Koikoi Ben','Kampala',770034343,20020143355,4040,'Stanbic','Makerere')
customer5=Customer(1424,'Anying jamin','Kampala',773488343,2002012454,4040,'Stanbic','Makerere')
customer6=Customer(5342,'Cap Benja','Kampala',773435543,200355444,4040,'Stanbic','Makerere')
customer7=Customer(8576,'Awilo Beniface','Kampala',773004343,20024564553,4040,'Stanbic','Makerere')
customer8=Customer(8465,'Kakaire Johnson','Kampala',773411343,224545441414,4040,'Stanbic','Makerere')
customer9=Customer(3684,'Opolot Patrick','Kampala',773433343,263444141414,4040,'Stanbic','Makerere')
customer10=Customer(9476,'Acom Cathey','Kampala',773412343,643544141414,4040,'Stanbic','Makerere')
customer11=Customer(2497,'Irwe Collins','Kampala',773434343,33320141414,8080,'Centenary','Kampala')
customer12=Customer(8456,'Murindanyi Sudi','Kampala',777834388,44440141414,8080,'Centenary','Kampala')
customer13=Customer(1324,'Emojong joseph','Kampala',773434377,666620141414,8080,'Centenary','Kampala')
customer14=Customer(5533,'Olowo Auther','Kampala',773434366,2033520141414,8080,'Centenary','Kampala')
customer15=Customer(4466,'Clief Ben','Kampala',773434355,355440141414,8080,'Centenary','Kampala')
customer16=Customer(2233,'Mugegwa Jordan','Kampala',773434323,2003350141414,8080,'Centenary','Kampala')
customer17=Customer(6677,'Ahena Priscilla','Kampala',700434343,200201644314,8080,'Centenary','Kampala')
customer18=Customer(9988,'Nandaula Philomena','Kampala',705434343,200201355314,8080,'Centenary','Kampala')
customer19=Customer(2200,'Akello Clair','Kampala',700034343,203143443414,8080,'Centenary','Kampala')
customer20=Customer(5745,'Slay Queen','Kampala',7734343,2004455341414,8080,'Centenary','Kampala')








        
    
    
