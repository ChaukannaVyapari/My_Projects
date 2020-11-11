from time import sleep
p = {"pin":1234}

def atm():
    balance = 500000.0
    foreward_balance  = 0
    min_balance = 1000.0
    print("***** WELCOME TO BLA-BLA-BLA BANK ATM *****")
    passcode = int(input("ENTER PIN: "))
    while True:
        if passcode == p["pin"]:
            print("SELECT: ")
            print("1.) CHECK BALANCE\n2.) WITHDRAW\n3.) DEPOSIT\n4.) CHANGE PIN\n5.) EXIT")
            option = int(input("ENTER YOUR OPTION: "))
            if option == 1:
                print("please wait...")
                sleep(3)
                print("YOUR BALANCE IS: ",balance)
            elif option == 2:
                w_money = float(input("ENTER AMOUNT TO BE WITHDRAWN: "))
                if w_money > balance:
                    print("please wait...")
                    sleep(3)
                    print("FUND NOT AVAILABLE, AMOUNT EXCEEDS TOTAL AMOUNT THERE IN THE ACCOUNT")
                else:
                    if (balance - w_money > 1000):
                        foreward_balance = balance - w_money
                        balance = foreward_balance
                        print("please wait...")
                        sleep(3)
                        print("AMOUNT WITHDRAWN, TOTAL BALANCE NOW IS: ",foreward_balance)
                    else:
                        print("please wait...")
                        sleep(3)
                        print("YOUR BALANCE MUST NOT GO BELOW 1000 BUCKS...")
                        continue
            elif option == 3:
                w_money2 = float(input("ENTER AMOUNT TO BE DEPOSITED: "))
                foreward_balance2 = balance + w_money2
                balance = foreward_balance2
                print("please wait...")
                sleep(3)
                print("AMOUNT DEPOSITED, TOTAL BALANCE NOW IS: ",foreward_balance2)
            elif option == 4:
                print("please wait...")
                sleep(3)
                pinChange()
            elif option == 5:
                print("VISIT AGAIN, HAVE A NICE DAY...")
                exit()

        else:
            print("EITHER OF THE USERNAME OR PASSWORD IS WRONG, TRY AGAIN...")
            con = input("WANT TO TRY AGAIN, ENTER YES/NO: ")
            if con.lower() == 'yes':
                atm()
            else:
                print("VISIT AGAIN, HAVE A NICE DAY...")
                exit()

def pinChange():
    o_pin = int(input("ENTER PREVIOUS PIN: "))
    if (o_pin == p["pin"]):
        pin2 = int(input("ENTER NEW PIN: "))
        c_pin2 = int(input("TO CONFIRM, ENTER THE NEW PIN AGAIN: "))
        if pin2 == c_pin2:
            p["pin"] = c_pin2
            print("PIN IS CHANGED, PLEASE TAKE YOUR CARD OUT AND LOGIN AGAIN...")
            sleep(3)
            atm()
        else:
            print("THE TWO PINS DID NOT MATCH, TRY AGAIN...")
            yn = input("WANT TO TRY AGAIN, YES/NO: ")
            if yn.lower() == "yes":
                pinChange()
            else:
                
                exit
    else:
        print("INCORRECT PIN, TRY AGAIN...")
        pinChange()
                            

#Calling the Function
atm()
