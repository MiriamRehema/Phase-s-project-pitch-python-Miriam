from model import list_accounts, get_password
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
    choice = input("Enter your choice (1/2): ")
#if your choice is an account
    if choice == "1":
        display_accounts()
    elif choice == "2":
        #and its password you should input the account name so that it displays its password
        account = input("Enter the account name: ")
        display_password(account)
        #if the account name does not exist it will print an invalid choice since its not there
    else:
        print("Invalid choice. Please select 1 or 2.")
