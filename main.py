import random
import sqlite3
from datetime import datetime

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.- /\\?+*# "

upper, lower, nums, syms = True, True, True, True # Can set as false and the compiler will not include the specific characters in the password
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 8 # the length of characters in the password
amount = 10 # the number of passwords one can generate

# Database setup
connect = sqlite3.connect('passwords.db')
c = connect.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT NOT NULL
    )
''')

# Generate passwords and store them in the database

for x in range(amount):
    passwrd = "".join(random.sample(all, length))
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tag = "example_tag"
    print(passwrd)

    c.execute('Insert into passwords (password) values (?)', (passwrd,))

connect.commit()
connect.close()
    