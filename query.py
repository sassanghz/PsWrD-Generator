import sqlite3

connect = sqlite3.connect('passwords.db')
c = connect.cursor()

# Query to select all passwords
c.execute('SELECT * FROM passwords')
all_passwords = c.fetchall() # ensure that the data is present
print("All Passwords:", all_passwords)

connect.close()
