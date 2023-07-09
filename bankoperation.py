#bankoperation
#data to collect = first name, last name, email address, password
#login details - account number and password
import random
userID = {} #dictionary

def init ():
    
    print ("welcome to BankPHP") 
    validoption = False
    while validoption == False:
        haveaccount = int(input("Do you have an acoount with us? \n 1. Yes \n 2. No \n"))
        if (haveaccount == 1):
            validoption = True
            login ()
        elif (haveaccount == 2):
            validoption = True
            #register () - this will actually just run the code
            print (register()) #this will both run the code and print ((display)) other functions in the code
        else:
            print ("Please select a valid option")
def register():
    print ("*****REGISTER*****")
    email = input ("Please enter your email address: \n")
    first_name = input ("please enter your first name:\n")
    last_name = input ("please enter your last name:\n")
    password = input ("Please choose a password\n")
    accountnumber = random.randrange (0000000000,9999999999)
    userID = [first_name, last_name, email, password]
    
    print ("your account has been ssccesfully created")
    print ("your account number is  %d" %accountnumber)

    login()

def login():
    print ("*****Login to your account******")
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        accountnumber = random.randrange (0000000000,9999999999)
        accountnumberfromuser = int(input("Please enter your account number:\t"))
        passwordfromuser = input("Please enter your password:\t")
        if (passwordfromuser in userID[accountnumberfromuser]):
            if accountnumber == accountnumberfromuser:
                if(userID[3] == passwordfromuser):
                    isLoginSuccessful = True
            else:
                print ("Invalid details")
                print (accountnumber)
                print (accountnumberfromuser)
                print (userID)



    
    BankOperations()

def BankOperations():
    print ("What do you want to do?")

#def accNoGen():
    
    

init()
#print (accNoGen())



