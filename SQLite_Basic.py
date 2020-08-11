import sqlite3

# Creating a connection
# db file create in same path where program is run
conn = sqlite3.connect('database.db')

# Auto Commit
conn.isolation_level = None

# Creating a cursor
c = conn.cursor()

# Create table statement
statement = "CREATE TABLE user (userid INTEGER PRIMARY KEY AUTOINCREMENT, website TEXT NOT NULL, username TEXT NOT NULL, pwd TEXT NOT NULL)"
c.execute(statement)


# Insert value
statement = 'INSERT INTO user VALUES (1, "fb", "pratik", "pratik123")'
c.execute(statement)

statement = [
    ("Gmail", "pratik@gmail.com", "pratik123"),
    ("github", "pratikv", "pratik"),
    ("linkedin", "Pratik@gmail.com", "linkedmail")
]
c.executemany("INSERT INTO user (website, username, pwd) VALUES (?, ?, ?)", statement)

# Commiting
# conn.commit()

# Display values
statement = 'SELECT * FROM user'
result = c.execute(statement)

# Table Header
header = [res[0] for res in result.description]
print(header)
# Values
for row in result:
    print(row)

conn.close()