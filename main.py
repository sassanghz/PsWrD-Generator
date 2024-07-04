import random
import sqlite3
from datetime import datetime

# Character sets
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.- /\\?+*# "

# Configuration for character inclusion
upper, lower, nums, syms = True, True, True, True
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 8  # The length of characters in the password
amount = 10  # The number of passwords to generate

# Database setup
connect = sqlite3.connect('passwords.db')
c = connect.cursor()

# Drop the existing table if it exists
c.execute('DROP TABLE IF EXISTS passwords')

# Create table with new schema
c.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT NOT NULL,
        created TEXT NOT NULL,
        tag TEXT
    )
''')

# Generate passwords and store them in the database
for x in range(amount):
    password = "".join(random.sample(all, length))
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tag = "example_tag" # this can be modified
    print(password)

    # Insert password with metadata into the database
    c.execute('INSERT INTO passwords (password, created, tag) VALUES (?, ?, ?)', (password, created, tag))

connect.commit()
connect.close()
