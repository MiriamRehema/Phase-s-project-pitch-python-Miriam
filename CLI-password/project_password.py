# password_manager.py

import click
from model import add_password, get_password, list_accounts

@click.group()
def cli():
    """Password Manager CLI"""
    pass

@cli.command()
@click.argument("account")
@click.argument("password")
def add(account, password):
    """Add a new password"""
    add_password(account, password)
    click.echo(f"Password for {account} added successfully.")

@cli.command()
@click.argument("account")
def get(account):
    """Retrieve a password"""
    password = get_password(account)
    if password:
        click.echo(f"Password for {account}: {password}")
    else:
        click.echo(f"No password found for {account}.")

@cli.command()
def list():
    """List all saved accounts"""
    accounts = list_accounts()
    if accounts:
        click.echo("Saved accounts:")
        for account in accounts:
            click.echo(account)
    else:
        click.echo("No accounts saved.")

if __name__ == "__main__":
    cli
