# Phase-s-project-pitch-python-Miriam
## MY PASSWORD MANAGER
My Password Manager is a simple command-line application for managing and storing your passwords securely.

## Table of Content

Dependancies
Technology Used
Licence
Authors Info

## Dependencies
Before you begin, ensure you have the following dependencies installed:

1.Python 3.x: You can download Python from the official Python website.

2.SQLAlchemy: This library is used for database operations. Install it using pip:
a.pip install sqlalchemy

# Click: Click is used for creating the command-line interface. Install it using pip:
b.pip install click

## Technology used
The challenge was mainly based on Python, so I used the following technologies:
- Python(your version)

Getting Started
# Follow these steps to set up and use My Password Manager:

# Clone the Repository

Clone the My Password Manager repository to your local machine:
`git clone <git@github.com:MiriamRehema/Phase-s-project-pitch-python-Miriam.git>`

`cd My-Password-Manager`

`Initialize the Database`

Run the following command to create the SQLite database for storing passwords:
$`python model.py`
Seed the Database (Optional)

You can populate the database with some initial data by running:

python seed.py
This step is optional but can be useful for testing.
# Manage Passwords

You can now use the following commands to manage your passwords:

Add a Password: To add a new password, run the following command:

python password_project.py add <account> <password>

Retrieve a Password: To retrieve a password, run the following command:

python password_project.py get <account>

List All Accounts: To list all saved accounts, run:

python password_project.py list

Delete a Password: To delete a password for a specific account, run:

python password_project.py delete <account>
Usage Examples
Here are some usage examples of the My Password Manager commands:

Adding a Password:
python password_project.py add example<_account example_password>

Retrieving a Password:
python password_project.py get <example_account>

Listing All Accounts:
python password_project.py list

Deleting a Password:
python password_project.py delete example_account

Note

Passwords are stored securely in the SQLite database.

It's recommended to keep your database file (passwords.db) secure and backed up.

Contributing
Feel free to contribute to this project by opening issues or creating pull requests.

# License

This project is open-source and available under the MIT License.
MIT License
Copyright (c) 2023 MiriamRehema

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
