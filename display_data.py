from model import list_accounts, get_password,delete_password,add_password
#defining the fuction
def display_accounts():
    #the accounts should be equal to the list_accounts
    accounts = list_accounts()
    if accounts:
        print("Saved accounts:")
        for account in accounts:
            print(account)
            #if not equal it should print this
    else:
        print("No accounts saved.")
#a function to display a password for a specific account
def display_password(account):
    password = get_password(account)
    if password:
        print("Password for {}: {}".format(account, password))
        #otherwise print this
    else:
        print("No password found for {}.".format(account))

if __name__ == "__main__":
    print("My Password Manager - Display Data")
    
    print("1. Display All Accounts")
    print("2. Display Password for an Account")
    print("3. Delete password")
    print("4. Add a password")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
#if your choice is an account
    
    if choice == "1":
        display_accounts()
    elif choice == "2":
        #and its password you should input the account name so that it displays its password
        account = input("Enter the account name: ")
        display_password(account)
        #if the account name does not exist it will print an invalid choice since its not there
    elif choice=="3":
        account=input("Entre account name: ")
        delete_password(account)
    elif choice=="4":
        account=input("Entre an account name:")
        password=input("Entre a password:")
        add_password(account,password)
    elif choice=="5":
        print("You have now exited")

    else:
        print("Invalid choice. Please select 1 ,2,3,4 or 5")
