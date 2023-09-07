from model import list_accounts, get_password

def display_accounts():
    accounts = list_accounts()
    if accounts:
        print("Saved accounts:")
        for account in accounts:
            print(account)
    else:
        print("No accounts saved.")

def display_password(account):
    password = get_password(account)
    if password:
        print("Password for {}: {}".format(account, password))
    else:
        print("No password found for {}.".format(account))

if __name__ == "__main__":
    print("Password Manager - Display Data")
    print("1. Display All Accounts")
    print("2. Display Password for an Account")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        display_accounts()
    elif choice == "2":
        account = input("Enter the account name: ")
        display_password(account)
    else:
        print("Invalid choice. Please select 1 or 2.")
