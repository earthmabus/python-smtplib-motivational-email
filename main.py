import email_account
import random
import datetime as dt

my_email = "earthmabus@gmail.com"

PASSWORD_FILE = "./password.txt"
QUOTES_FILE = "./quotes.txt"

def load_password():
    '''loads the password for the email account from PASSWORD_FILE'''
    retval = ""
    with open(PASSWORD_FILE, "r") as file_password:
        retval = file_password.readline().strip()
    return retval


# load the inspirational quotes from the QUOTES_FILE
def load_quotes():
    retval = []
    with open(QUOTES_FILE, "r") as file_quotes:
        quotes = file_quotes.readlines()

        for q in quotes:
            items = q.split("-")
            retval.append((items[0].strip(), items[1].strip()))
    return retval

# load the quotes and choose a random one to send
quotes = load_quotes()
chosen_quote = random.choice(quotes)

# acquire the password for the account
password = load_password()

# acquire the date
now = dt.datetime.now()

# send an email
account = email_account.EmailAccount(my_email="earthmabus@gmail.com", my_password=password)
account.send_email("earthmabus@hotmail.com", f"Inspirational Quote of the Day ({now.year}/{now.month}/{now.day})", f"{chosen_quote[0]}\nby {chosen_quote[1]}")
