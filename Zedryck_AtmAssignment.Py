import time
import os
Accounts = ["TestAccount"]
Passwords =["TestPassword"]

def Typing(NameStr,TimeS):
    for x in str(NameStr):
        print(x, end="",flush=True)
        time.sleep(TimeS)
    print("")


def Clear_Screen():
    if os == 'nt':
        os.system('cls')
    else:
        os.system('clear')
Clear_Screen()

def RandomDots(SequenceOfDots):
    for i in range(1,SequenceOfDots):
        Clear_Screen()
        Typing("...",1)
        Clear_Screen()

ChosenInput1 = 0
ExistingAccounts = 1


#I SPENT TOO LONG ON THIS HELP

# YOU CAN CREATE AN ACCOUNT AND LOG THAT IN, BUT IF YOU FORGET I DIDN'T MAKE A FORGET PASSWORD ):

#YOU CAN ALOST LOG IN USING TESTACCOUNT with TESTPASSWORD
#ALSO TECHNICALLY YOU CAN PUT A 4 DIGIT PASSWORD (THERE IS NO LIMIT TO PASSWORD MAKING Xd) 
#ERM YOU CAN MAKE THE SAME NAME WITH ACCOUNT. BUT IT WILL ALWAYS ACCESS THE FIRST ACCOUNT IT WAS EVERY MADE-
#I HAVE YET TO DISABLE PEOPLE FROM MAKING ACCOUNTS OF THE SAME USER ):
# IM NO SMART ENOUGH, OK THANK YOU- BYE

while True:
    while True:
        try:
            loginSuccessful = False
            Typing("Welcome User, please choose an input!",0.01)
            Typing("1. Login",0.01)
            Typing("2. Register",0.01)
            Chosen = int(input(""))
            ChosenInput1 = Chosen
            Clear_Screen()
            if Chosen == 1:
                Typing("Switching screen.",0.01)
                time.sleep(1)
                RandomDots(2)
                break
            elif Chosen == 2:
                Typing("Switching screen.",0.01)
                time.sleep(1)
                RandomDots(2)
                break
            else:
                Typing("The input was invalid, please try again.",0.01)
                time.sleep(1)
                Clear_Screen()
                continue
        except:
            Typing("The input failed, please try again.",0.01)
            time.sleep(1)
            Clear_Screen()
            continue

    if ChosenInput1 == 1:
        while True:
            Typing("Please Type in your username.",0.01)
            UsernameInput = str(input(""))
            Clear_Screen()        
            AccountFound = False

            AccountNumber = 0

            for x in range(0,ExistingAccounts + 1):
                #print(str(x))
                AccountNumber = int(x)
                try:
                    if str(UsernameInput) == str(Accounts[x]):
                        AccountFound = True
                except:
                    continue

            
            if AccountFound == True:
                Typing("Account located, please enter your password.",0.01)

                Password = str(input(""))
                
                if str(Password) == str(Passwords[AccountNumber-1]):
                    loginSuccessful = True
                    
                if loginSuccessful == True:
                    Typing("Account Access, Welcome!",0.01)
                    break
                   

            elif AccountFound == False:
                Typing("Acount was not found, please try again. Type '1' to go to the start, enter to retry.",0.01)
                try:
                    LeaveInp = int(input(""))
                    Clear_Screen()
                    if LeaveInp == 1:
                        break
                    continue
                except:
                    Clear_Screen()
                    continue
    
    if ChosenInput1 == 2:
        while True:
            try:
                Typing("Please choose a username to use!",0.01)
                Chosen = str(input(""))
                Typing("Are you sure of using:",0.01)
                print("")
                print("")
                Typing(Chosen,0.01)
                print("")
                Typing("1. Yes",0.01)
                Typing("2. No",0.01)

                FastInpAns = 0
                while True:
                    try:
                        FastInp = int(input(""))
                        FastInpAns = FastInp
                        if FastInp == 1:
                            ExistingAccounts += 1
                            print("Account Created!")
                            Accounts.append(Chosen)
                            break
                        elif FastInp == 2:
                            break
                        else:
                            Typing("Input failed, please try again!",0.01)
                            continue
                    except:
                        Typing("Input failed, please try again",0.01)
                        continue
                if FastInpAns == 1:
                    print("Ok!, please give us a Password for the account!")   
                    while True:
                        try:
                            ChosenPass = str(input(""))
                            Typing("Are you sure of using:",0.01)
                            print("")
                            print("")
                            Typing(ChosenPass,0.01)
                            print("")
                            Typing("1. Yes",0.01)
                            Typing("2. No",0.01)

                            FastInpAns = 0
                            while True:
                                try:
                                    FastInp = int(input(""))
                                    FastInpAns = FastInp
                                    if FastInp == 1:
                                        print("Password Chosen! Please log in now!")
                                        Passwords.append(ChosenPass)
                                        break
                                    elif FastInp == 2:
                                        break
                                    else:
                                        Typing("Input failed, please try again!",0.01)
                                        continue
                                except:
                                    Typing("The input failed, please try again.",0.01)
                                    time.sleep(1)
                                    Clear_Screen()
                                    continue
                            break
                        except:
                            Typing("The input failed, please try again.",0.01)
                            time.sleep(1)
                            Clear_Screen()
                            continue
                elif FastInpAns == 2:    
                    continue
                break
            except:
                Typing("The input failed, please try again.",0.01)
                time.sleep(1)
                Clear_Screen()
                continue    
                    

    if loginSuccessful == True:
        Typing("Hold on as I Check your Balance.",0.01)
        time.sleep(3)
        RandomDots(3)
        Typing("0 dollars found, Wow your poor as heck!",0.01) #For school appropriating, I did not curse. :)
        Typing("But that's ok, being broke isn't that bad!",0.01)
        time.sleep(3)
        Clear_Screen()
        Typing("Your problebly so embarrassed from being so poor, let me log you out!",0.01)
        Typing("Loging out of account.",0.01)
        time.sleep(3)
        RandomDots(3)
        continue

            