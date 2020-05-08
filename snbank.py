import random
import sys
import time

def welcome():
    login()


def logged():
    user = input("Please enter your username: ")
    passw = input("Please enter your password: ")

    for line in open("staff.txt", "r").readlines():
        info = line.split()

        if user == info[0] and passw == info[1]:
            print("Succesfully Logged in")
            print("Hello, " + info[0])
            successLogin()

    else:
        print("Incorrect Login Details. Try Again...")
        logged()
 



def login():
    print("""
            1 - Staff Login
            2 - Close App 
    """)
    option = int(input("[1/2]: "))
    if option == 1:
        logged()

    else:
        print("The App is shutting down, please wait....")
        rem = open("customer.txt", "w").close()
        time.sleep(3)
        print("Sessions successfully deleted...")
        print("Goodbye... Thanks for Banking with us.")
        sys.exit()



def successLogin():
    print("""
            1 - Create New Bank Account
            2 - Check Account Details
            3 - LogOut
    """)

    choice = int(input("[1/2/3]: "))
    if choice == 1:
        name = input("Please enter your preferred account name: ")
        bal = float(input("Please enter your opening balance: "))
        acct_type = input("Please enter your preferred account type: ")
        email = input("Please enter your account email: ")


        balance = str(bal)

        data = open("customer.txt", "a")
        data.write(name)
        data.write("\n")
        data.write(balance)
        data.write("\n")
        data.write(acct_type) 
        data.write("\n")
        data.write(email)
        data.write("\n")

        acct_number = str(random.randrange(10**9, 10**10))

        data.write(acct_number)
        data.close()
        print("Your Account Details have been successfully Logged.")
        print("This is your account Number: " + acct_number )
        successLogin()

    elif choice == 2:
        print("To check your Account Details")
        digit = input("Log your Account number: ")

        line = open("customer.txt", "r").readlines()[4]
        print()
        if digit == line:
            print("Account Name: " +open("customer.txt", "r").readlines()[0])
            print("Opening Balance: " + open("customer.txt", "r").readlines()[1])
            print("Account Type: " + open("customer.txt", "r").readlines()[2])
            print("Account Email: " + open("customer.txt", "r").readlines()[3])
            successLogin()

        else:
            print("Not found!!")
            successLogin()

    else:
        print("Please Wait... Loading...")
        time.sleep(2)
        login()


welcome()