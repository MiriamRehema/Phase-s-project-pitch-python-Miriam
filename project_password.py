# project_password.py

import click
from model import add_password, get_password, list_accounts,delete_password
#using click
@click.group()
def cli():
    """Password Manager CLI"""
    pass
#The first command when you want to add an account and a password
@cli.command()

#the arguments each of them
@click.argument("account")
@click.argument("password")
def add(account, password):
    """Add a new password"""

    #The command itself
    add_password(account, password)
    click.echo("Password for {} added successfully.".format(account))

#The second command when you want to retrieve a password
@cli.command()
@click.argument("account")
#The command as a function
def get(account):
    """Retrieve a password"""
    # the password should  match the account
    
    password = get_password(account)
    if password:
        #If it matches it should display the gotten password
        click.echo("Password for {}: {}".format(account, password))

    else:
        #print this if the account does not match the password
        click.echo("No password found for {}.".format(account))

#The third command if you want a list of all saved account
@cli.command()
#The function itself
def list():
    """List all saved accounts"""
    #The accounts should be equal to what is in the list account
    accounts = list_accounts()
    if accounts:
        click.echo("Saved accounts:")
        for account in accounts:
            click.echo(account)
    else:
        click.echo("No accounts saved.")

#The 4rth command when you want to delete an account with its password
@cli.command()
#The argument(account)
@click.argument("account")
def delete(account):
    """Delete a password"""
    delete_password(account)
    #Hence deleting the password for a specific account
    click.echo("Deleted password for {}.".format(account))

# is a conditional statement that checks if the script is being run as the main program 
if __name__ == "__main__":
    cli
#For example, in your script, cli is a Click command group. When you run the script directly (e.g., python password_project.py),
#  the cli command group is defined and the Click commands are available for use in the command line. 
# If you were to import this script as a module into another Python script, the Click commands wouldn't be executed automatically unless you explicitly call them