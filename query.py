import sqlite3

connect = sqlite3.connect('passwords.db')
c = connect.cursor()

# Query to select all passwords 
c.execute('Select * from passwords')

# Fetch all results

passwords = c.fetchall()

# Print the passwords

for row in passwords:
    print(f"ID: {row[0]}, Password: {row[1]}")

connect.close()