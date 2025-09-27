import email_account

my_email = "earthmabus@gmail.com"

PASSWORD_FILE = "./password.txt"

def load_password():
    '''loads the password for the email account from PASSWORD_FILE'''
    retval = ""
    with open(PASSWORD_FILE, "r") as file_password:
        retval = file_password.readline().strip()
    return retval

password = load_password()

# send an email
account = email_account.EmailAccount(my_email="earthmabus@gmail.com", my_password=password)
account.send_email("earthmabus@hotmail.com", "Testing from Python application", "testing my refactor")


import datetime as dt

now = dt.datetime.now()
print(now)

date_of_birth = dt.datetime(year=1978, month=1, day=2)
print(date_of_birth)

