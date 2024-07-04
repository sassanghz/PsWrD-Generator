import sqlite3

tagToSearch = "example_tag"

connect = sqlite3.connect('passwords.db')
c = connect.cursor()

# Query to select passwords with a specific tag
c.execute('SELECT * FROM passwords WHERE tag=?', (tagToSearch,))

# Fetch all results

passwords = c.fetchall()

# Print the passwords

for row in passwords:
    print(f"ID: {row[0]}, Password: {row[1]}, Created At: {row[2]}, Tag: {row[3]}")
connect.close()