import email_account
import random
import datetime as dt
import os

QUOTES_FILE = "./quotes.txt"
GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

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

# acquire the date
now = dt.datetime.now()

# send an email
account = email_account.EmailAccount(my_email=GMAIL_ADDRESS, my_password=GMAIL_PASSWORD)
account.send_email("earthmabus@hotmail.com", f"Quote of the Day ({now.year}/{now.month}/{now.day})", f"{chosen_quote[0]}\n\nby {chosen_quote[1]}")
